from sys import exit

def ht(cx,cy,x,y,h):
	return h+abs(x-cx)+abs(y-cy)

n=int(input())			#高々100なのでほとんどが高さ0っていう状況はない
xyh=[0]*n

for i in range(n):
	x,y,h=map(int,input().split())
	xyh[i]=[x,y,h]
xyh.sort(key=lambda x:x[2],reverse=True)			#h=0を選択してしまうことを避ける

for cx in range(101):
	for cy in range(101):
		H=ht(cx,cy,xyh[0][0],xyh[0][1],xyh[0][2])
		for i in range(1,n):
			if max(H-abs(xyh[i][0]-cx)-abs(xyh[i][1]-cy),0)!=xyh[i][2]:			#H=ht(このfor文で選択した座標)にすると、高さ0の場合に合わなくなる
				break
			
		else:			#直前のifが行われなければ、という意味。forの外における
			print(cx,cy,H)
			exit()