n=int(input())
a=list(map(int,input().split()))

s=[0]*(n+1)
for i in range(n):
  s[i+1] = s[i] + a[i]

result = 10**10
for i in range(1,n):
  snuke = s[i]
  arai = s[n] - s[i]
  result = min(result, abs(snuke-arai))
print(result)