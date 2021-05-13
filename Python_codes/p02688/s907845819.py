n, k = map(int, input().split())

m = [0]*n

for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in range(d):
        m[a[j]-1] += 1

print(m.count(0))



