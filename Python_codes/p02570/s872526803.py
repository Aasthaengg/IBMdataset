D, T, S = map(int, input().split())

answer = D / S

if T >= answer:
    print('Yes')
else:
    print('No')