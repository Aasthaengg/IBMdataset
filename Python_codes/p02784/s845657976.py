H, N = map(int, input().split())
A = list(map(int, input().split()))

attack = sum(A)

if H <= attack:
    print('Yes')
else:
    print('No')