N = int(input())
B = list(map(int, input().split()))
ans = []
for i in range(N):
    last = 0
    for j, b in enumerate(B, 1):
        if b == j:
            last = b
    if last == 0:
        print(-1)
        exit()
    else:
        ans.append(B.pop(last - 1))
[print(a) for a in ans[::-1]]