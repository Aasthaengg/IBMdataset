N = int(input())
A = int(input())
if A >= (N - (N // 500) * 500):
    print('Yes')
else:
    print('No')
