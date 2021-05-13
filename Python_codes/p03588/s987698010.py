n=int(input())
temp = 10**10
for i in range(n):
    a,b=map(int,input().split())
    temp = min(temp,a+b)
print(temp)