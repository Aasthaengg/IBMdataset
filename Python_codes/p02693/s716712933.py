K = int(input())
A, B = map(int, input().split())

if K == 1:
    print('OK')
elif B - (B % K) >= A:
    print('OK')
else:
    print('NG')
