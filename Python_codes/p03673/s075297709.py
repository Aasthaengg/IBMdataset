n = int(input())
a = list(map(int, input().split()))

if n%2 == 0:
  ans = [str(a[n-1-i*2]) for i in range(n//2)] + [str(a[j*2]) for j in range(n//2)]
else:
  ans = [str(a[n-1-i*2]) for i in range(n//2+1)] + [str(a[1+j*2]) for j in range(n//2)]

print(' '.join(ans))
