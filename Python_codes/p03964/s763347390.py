n=int(input())
a=1
b=1
for i in range(n):
    ti,ai=map(int,input().split())
#    m=max(int((a-1)/ti)+1,int((b-1)/ai)+1)
    m=max(int((a-1)//ti)+1,int((b-1)//ai)+1)
    a=m*ti
    b=m*ai
print(a+b)