n = int(input())
k = int(input())
x = list(map(int,input().strip().split()))

ans = 0
for i in x:
  ans += min(2*abs(i-k),2*abs(i))
print(ans)