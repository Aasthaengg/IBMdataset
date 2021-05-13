N = int(input())
A = sorted(map(int, input().split()))
M = max(A)
cs = [0]
for i in A:
    cs.append(cs[-1] + i)
A.append(A[-1])
ans = 0
for i in range(N, 0, -1):
    if cs[i] * 2 >= A[i]:
        ans += 1
    else:
        break
print(ans)