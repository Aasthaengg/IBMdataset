N = int(input())
L = list(map(int, input().split()))

maxlength = max(L)
total = sum(L)
if total > maxlength * 2:
    print('Yes')
else:
    print('No')