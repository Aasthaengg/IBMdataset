a,b,n=map(int,input().split())
x=min(b-1,n) #上記よりxとしてmin(B-1,N)を選ぶのが最善
print((a*x)//b-a*(x//b))