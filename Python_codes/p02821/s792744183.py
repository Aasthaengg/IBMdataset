#降順ソートの方がうまくいきそう
n,m=map(int,input().split())
a=sorted(list(map(int,input().split())),reverse=True)
cs=[]
sum=0
for i in range(n):
	sum+=a[i]
	cs.append(sum)

#和が引数以上の場合をカウントする
def overX(x):
	count=0
	#両手が違う人を握るときのみ考える
	if a[0]*2<x:
		return 0
	else:
		for i in range(n):
			if a[i]+a[0]<x:
				count+=0
			else:
				lb, ub = 0, n
				#パターンAのにぶたん。左がOなので[lb,ub)で持つ。
				while ub-lb>1:
					mid=(lb+ub)//2
					if a[i]+a[mid]>=x:
						lb=mid
					else:
						ub=mid
				count+=lb+1
		return count
#print(overX(130))

#overX>=mなる最大のxを探す->xは小さい方が実現しやすいのでパターンA->[lb,ub)でもつ
lb=1 #実現しやすい方
ub=2*10**5+1
while ub-lb>1:
	mid=(ub+lb)//2
	if overX(mid)>=m:
		lb=mid
	else:
		ub=mid
#ub=overX(x)>=mなる最小のx。これ以上大きくするとmに満たなくなる。
maxx=lb

hp=0
#maxx+1以上の要素をすべてたす
#和がmaxx+1以上になる組み合わせの数だけhpを加え、countをインクリメントする
if a[0]*2>=maxx+1:
	for i in range(n):
		if a[i]+a[0]<maxx+1:
			break
		else:
			lb, ub = 0, n
			#パターンAのにぶたん。左がOなので[lb,ub)で持つ。
			while ub-lb>1:
				mid=(lb+ub)//2
				if a[i]+a[mid]>=maxx+1:
					lb=mid
				else:
					ub=mid
			#a[0]からa[lb]は、a[i]と足した時にx以上になり条件を満たす。
			hp+=a[i]*(lb+1)+cs[lb]
hp+=(m-overX(maxx+1))*maxx
print(hp)