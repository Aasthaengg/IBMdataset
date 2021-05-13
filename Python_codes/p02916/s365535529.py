a=int(input())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
o=list(map(int,input().split()))
result1=0

for i in range(0,a-1):
    if n[i]+1==n[i+1]:
        result1+=o[n[i]-1]

for i in range(a):
    result1+=m[n[i]-1]
print(result1)