def mht(a,b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])
n,m=map(int,input().split())
p=[list(map(int,input().split())) for _ in range(n)]
c=[list(map(int,input().split())) for _ in range(m)]
#print(p)
#print(c)
for i in p:#全ての人に対してループ
	a=[10**9,0]#[最小距離、チェックポイントの番号]
	for j in range(m):#全てのチェックポイントに対してループ
		if mht(i,c[j])<a[0]:#最小距離を更新した場合
			a=[mht(i,c[j]),j+1]
	print(a[1])#i番目の学生が行くチェックポイント
