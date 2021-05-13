x,a,b=map(int,input().split())

flg=0
if b<a:
	b,a=a,b
	flg=1

ans = ["A","B"]

if 2*x<b+a:
	print(ans[flg])
else:
	print(ans[-1+flg])

