N = int(input())
A = list(map(int, input().split()))

ans = [0]*N
# 非破壊的に逆順で返す
for i in reversed(range(1, N+1)):
    v = A[i-1]
    # range(start, stop, step)
    for j in range(i, N+1, i):
        v += ans[j-1]
    # 箱に入れるかを決める
    ans[i-1] = v % 2

M = sum(ans)
print(M)
if M:
    # もし入っていれば、その添字に１を足して入れる。それをanpac
    print(*(i+1 for i, b in enumerate(ans) if b == 1))
