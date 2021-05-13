N, M = map(int, input().split())
v = M - N * 2
# print('v', v)
if v <= 0:
    print(M // 2)
    exit()
ans = N + v // 4
print(ans)
