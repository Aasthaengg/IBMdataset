import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = []
b = []
for _ in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
a.sort()
b.sort()
if n % 2 == 1:
    a_m = a[n // 2]
    b_m = b[n // 2]
    print(b_m - a_m + 1)
else:
    a_m = (a[n // 2 - 1] + a[n // 2]) #/ 2
    b_m = (b[n // 2 - 1] + b[n // 2]) #/ 2
    print(int(b_m - a_m) + 1) 


