import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

for i in range(1, n + 1):
    a[i-1] -= i

a.sort()
if n % 2 == 0:
    center = (a[n//2] + a[n//2-1]) // 2
else:
    center = a[(n-1)//2]
sub = lambda x: abs(x - center)
print(sum(list(map(sub, a))))
