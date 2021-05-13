n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

result = 0
for i in range(n):
  result += min(a[i]+a[i+1], b[i])
  a[i+1] = min(a[i+1], max(a[i]+a[i+1]-b[i],0))

print(result)