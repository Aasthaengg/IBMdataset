N = int(input())
a = list(map(int,input().split()))
sumA = 0
sumB = 0
for i in range(1,N+1):
    m = max(a)
    if i%2 == 1:
        sumA += m
    else:
        sumB += m
    a.remove(m)

print(sumA-sumB)

