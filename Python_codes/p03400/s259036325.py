n=int(input())
d,x=map(int,input().split())
for _ in range(n):
    a=int(input())
    for _ in range(1,d+1,a):x+=1
print(x)