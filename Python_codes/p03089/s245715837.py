n = int(input())
B = list(map(int, input().split()))
ans = []
for _ in range(n):
    for i in reversed(range(len(B))):
        if B[i] == i+1:
            x = B.pop(i)
            ans.append(x)
            break
if len(ans) == n:
    print(*ans[::-1], sep='\n')
else:
    print(-1)