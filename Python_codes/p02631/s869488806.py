n = int(input())
a = list(map(int,input().split()))

s = 0
for i in range(n):
    s ^= a[i]
print(' '.join([str(i^s) for i in a]))