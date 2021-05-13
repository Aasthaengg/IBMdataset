n = int(input())
k = int(input())
x = list(map(int, input().split()))

dist = 0
for i in range(n) :
    if x[i] > k - x[i] :
        dist += 2 * (k - x[i])
    else :
        dist += 2 * x[i]
print(dist)
