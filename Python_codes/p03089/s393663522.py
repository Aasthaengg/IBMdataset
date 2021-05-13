N = int(input())
B = list(map(lambda x: int(x) - 1, input().split()))
for i in range(N):
    if B[i] > i:
        print(-1)
        break
else:
    ans = []
    for _ in range(N):
        for i in range(len(B) - 1, -1, -1):
            if B[i] == i:
                ans.append(i)
                B = B[:i] + B[i + 1 :]
                break
    print("\n".join(map(lambda x: str(x + 1), ans[::-1])))
