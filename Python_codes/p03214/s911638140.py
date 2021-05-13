
n = int(input())
a = list(map(int,input().split()))
b = []
avg = sum(a)/len(a)

for i in range(n):
    b.append(abs(a[i] - avg))

print(b.index(min(b)))
