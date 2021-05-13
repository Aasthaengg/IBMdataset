N = int(input())
A = list(map(int,input().split()))
avg = 0
for a in A:
    avg += a
avg = avg / N
target = 1000
for a in A:
    dif1 = abs(target-avg)
    dif2 = abs(a-avg)
    if dif2 < dif1:
        target = a
ans = 0
for i,a in enumerate(A):
    if a == target:
        ans = i
        break
print(ans)