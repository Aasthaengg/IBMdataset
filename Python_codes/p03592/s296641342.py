N, M, K = map(int, input().split())
answer = set()
for i in range(M+1):
    # iは列で見たときの裏の数
    flipped = N*i
    for j in range(N+1):
        answer.add(flipped + ((M-i)-i)*j)

if K in answer:
    print('Yes')
else:
    print('No')
