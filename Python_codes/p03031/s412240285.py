n, m = list(map(int, input().split()))
k = []

for i in range(m):
    ki = list(map(int, input().split()))
    s = [0] * n
    for j in range(1, len(ki)):
        s[ki[j]-1] = 1

    k.append(int("".join(map(str, s)), 2))

p = list(map(int, input().split()))

def count1s(n):
    cnt = 0
    while n > 0:
        cnt += n & 1
        n >>= 1

    return cnt

cnt = 0
for i in range(2**n):
    sol = True
    for j in range(m):
        if count1s(i & k[j]) % 2 == p[j]:
            pass
        else:
            sol = False
            break

    if sol:
        cnt += 1

print(cnt)