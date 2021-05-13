a,b = map(int,input().split())
s = a + b
ans = s // 2
if s % 2 == 1: ans += 1
print(ans)