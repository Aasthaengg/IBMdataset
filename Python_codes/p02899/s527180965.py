n = int(input())
a = list(map(int,input().split()))
t = ['0'] * n

for i in range(n):
    t[a[i] - 1] = str(i + 1)

print(' '.join(t))