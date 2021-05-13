N = int(input())
B = list(map(int, input().split()))

ans = []

for k in range(N):
    flag = True
    for i, b in enumerate(reversed(B)):
        if N - k - i == b:
            ans.append(B.pop(b-1))
            flag = False
            break
    if flag:
        print(-1)
        exit()

for n in reversed(ans):
    print(n)