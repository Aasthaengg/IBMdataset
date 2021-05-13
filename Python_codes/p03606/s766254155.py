count=0
n=int(input())
for _ in range(n):
    i,r=map(int,input().split())
    count+=r-i+1
print(count)