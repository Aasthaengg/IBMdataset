x,a,b=map(int,input().split())
A=abs(x-a)
B=abs(x-b)
print("A" if A<B else "B")