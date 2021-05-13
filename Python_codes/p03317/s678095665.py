n, k = map(int,input().split())
a = [int(i) for i in input().split()]

if n == k:
    cnt = 1
else:
    cnt = (n - 2) // (k-1) + 1
print(cnt)