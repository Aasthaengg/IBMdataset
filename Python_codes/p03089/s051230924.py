N = int(input())
B = list(map(int, input().split()))

res = []
while len(B) > 0:
    idx = -1
    for i in range(len(B) - 1, -1, -1):
        if i + 1 == B[i]:
            idx = i
            break
    if idx == -1:
        print(-1)
        exit(0)
    else:
        res.append(B[idx])
        tmp = []
        for i, b in enumerate(B):
            if i != idx:
                tmp.append(b)
        B = tmp

for ans in res[::-1]:
    print(ans)
