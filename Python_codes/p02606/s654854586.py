L, R, d = [int(i) for i in input().split()]
cnt = 0
for x in range(L, R+1):
    cnt += 1 if x % d == 0 else 0
print(cnt)