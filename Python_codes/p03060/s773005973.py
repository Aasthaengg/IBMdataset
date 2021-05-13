n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
for v_i, c_i in zip(v, c):
  if v_i > c_i:
    ans += v_i - c_i
print(ans)