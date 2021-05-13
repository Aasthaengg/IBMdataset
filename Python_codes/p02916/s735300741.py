n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

temp = 9999
ans = 0
for i in a:
  ans += b[i-1]
  if i - temp == 1:
    ans += c[i-2]
  temp = i
  
print(ans)