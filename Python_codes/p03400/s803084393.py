n=int(input())
d,x=map(int,input().split())
a=[int(input()) for i in range(n)]
ans=[1+(d-1)//a[i] for i in range(n)]
print(x+sum(ans))

