n,x,t= map(int,input().split()) #標準入力

if(n%x==0):
	num=n//x
else:
	num=n//x+1

print(num*t) #焼くセット数*時間を計算して出力(())