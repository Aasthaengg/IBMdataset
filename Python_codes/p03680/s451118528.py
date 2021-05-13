n = int(input())
a_l = [ int(input()) for _ in range(n) ]

# N 1
ans = 0
next_idx = 0
for _ in range(n):
    ans += 1
    next_idx = a_l[next_idx]-1
    if next_idx == 1:
        break
if next_idx != 1:
    ans = -1
print(ans)