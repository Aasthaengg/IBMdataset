M = int(input())
B = [0] + list(map(int, input().split()))

ans = [0] * (M+1)
ret = []

for i in reversed(range(1, M+1)):
    if i > M / 2:
        ans[i] = B[i]
    else:
        if B[i] == sum(ans[i*2::i]) % 2:
            ans[i] = 0
        else:
            ans[i] = 1
    if ans[i] == 1:
        ret.append(i)

print(len(ret))
if len(ret) > 0:
    print(*ret[::-1])