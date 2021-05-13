from itertools import accumulate

N, K = map(int, input().split())
al = list(map(int, input().split()))
syusoku = [N] * N

for _ in range(K):
    s = [0] * N
    for i in range(N):
        left = i - al[i]
        right = i + al[i]
        if left < 0:
            left = 0
        s[left] += 1
        if right + 1 <= N - 1:
            s[right + 1] -= 1
        # print(left,right)
    al = list(accumulate(s))
    # print(al)
    if al == syusoku:
        print(*al)
        #print('end')
        exit()

print(*al)
