n = int(input())
k = int(input())
x = list(map(int, input().split()))
s = 0
for i in range(n):
    d = x[i] if x[i] < abs(k-x[i]) else abs(k - x[i])
    s += d*2
print (s)