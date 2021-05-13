import fractions
N, K = map(int, input().split())
arr = list(map(int, input().split()))
t = arr[0]
for i in range(1,N):
    t = fractions.gcd(t,arr[i])
if max(arr) < K or K % t != 0:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')