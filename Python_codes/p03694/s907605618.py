N = int(input())
a = [int(i) for i in input().split()]

a = sorted(a)
s = 0
for i in range(N-1):
    s += a[i+1] - a[i]

print(s)
