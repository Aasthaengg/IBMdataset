N = int(input())
S = input()
lb = 0
rw = S.count('.')
ans = rw
for s in S:
    if s == '.':
        rw -= 1
    else:
        lb += 1
    ans = min(ans, lb + rw)
print(ans)
