N = int(input())
ans = 0
for i in range(1,int(N**0.5)+1):
  x = N-i
  if x%i==0 and x//i>i:
    ans += x//i
print(ans)
