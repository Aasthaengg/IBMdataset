n=int(input())
l=list(map(int, input().split()))
v=sorted(l)
ans=(v[0]/(2**(n)))
for i in range(n):
  ans+=(v[i]/(2**(n-i)))
print(ans)
