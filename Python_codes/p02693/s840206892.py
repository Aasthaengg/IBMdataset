# We Love Golf
K = int(input())
A, B = map(int, input().split())
if K == 1:
    print('OK')
else:
    print(['NG', 'OK'][(B % K) <= (B - A)])