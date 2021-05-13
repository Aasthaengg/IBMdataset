N = int(input())
A = list(map(int, input().split()))

if sum(A) == 0:
    print("Yes")
    exit(0)

cnt = {}
for a in A:
    if a not in cnt:
        cnt[a] = 1
    else:
        cnt[a] += 1

if len(cnt) == 2:
    if cnt[0] == N // 3:
        print("Yes")
        exit(0)

if len(cnt) == 3:
    k1, k2, k3 = cnt.keys()
    v1, v2, v3 = cnt.values()
    if not (k1 ^ k2 ^ k3):
        if v1 == v2 and v2 == v3:
            print("Yes")
            exit(0)

print("No")
