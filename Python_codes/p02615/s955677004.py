import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

m = (n-1)//2

if (n-1) % 2 == 1:
    print(sum(a[:m]) + sum(a[1:m+1]) + a[m])
else:
    print(sum(a[:m]) + sum(a[1:m+1]))