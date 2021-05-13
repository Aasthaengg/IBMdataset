#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

x,k,d=input2()
abs_x=abs(x)
count=min(abs_x//d,k) #移動回数
abs_x-=d*count #到達点
rem=k-count


if rem>0:
	if rem%2==1:
		abs_x-=d #abs_x>=0は自明なので，-でok

ans=abs(abs_x)
print(ans)