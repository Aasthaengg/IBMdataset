n, k = map(int, input().split())
ps = list(map(int, input().split()))
acc = 0
for i in range(k):
    acc += ps[i]
max_a = acc
for i in range(1,n-k+1):
    acc -= ps[i-1]
    acc += ps[i+k-1]
    max_a = max(max_a, acc)
print((max_a+k)/2)