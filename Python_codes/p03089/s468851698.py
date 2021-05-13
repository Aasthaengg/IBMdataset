N = int(input())
B = list(map(int, input().split()))
ans = []
max_b = max(B)
for i in range(N):
    for b in range(max_b, 0, -1):
        if len(B) > b-1 and B[b-1] == b:
            ans += [B.pop(b-1)]
            break

if len(ans) != N:
    print(-1)
else:
    for a in ans[::-1]:
        print(a)
