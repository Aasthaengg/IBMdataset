
import sys
sys.setrecursionlimit(10000)

class UnionFindTree:
	def __init__(self,size):
		"""
		size個の集合を作成
		負の値は、ルートで集合の個数
		正の値は、次の要素
		"""
		self.table=[-1 for _ in range(size)]

	def find(self,x):
		"""
		グループ番号を取得
		"""
		# 本質的には、木を上に辿るだけ
		# ただし、通常、UnionFindでは経路圧縮を行うのが普通らしい
		if self.table[x] < 0:
			# 一個上がルートならば、それを返して終わり
			return x
		else:
			# そうでなければ、ルートまで辿るついでに経路圧縮
			self.table[x] = self.find(self.table[x])
			return self.table[x]
		return x

	# 併合
	def union(self,x,y):
		# s1,s2は正
		# table[s1],table[s2]は負
		s1=self.find(x)
		s2=self.find(y)
		if s1!=s2:
			# 個数が小さい方をルートにくっつける
			# ルートサイズは負なので、ルートが大きい方が個数が小さい?
			if self.table[s2]<=self.table[s1]:
				# s1が小さい
				self.table[s1]+=self.table[s2]
				self.table[s2]=s1
			else:
				# s2が小さい
				self.table[s2]+=self.table[s1]
				self.table[s1]=s2
			return True
		return False

	def groupCount(self):
		ret=0
		for i in range(len(self.table)):
			if self.table[i] < 0:
				ret+=1
		return ret

N,M=map(int,input().split())

UF=UnionFindTree(N)

for _ in range(M):
	A,B=map(int,input().split())
	UF.union(A-1,B-1)


print(UF.groupCount()-1)

