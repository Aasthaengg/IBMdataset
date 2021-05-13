n = int(input())
min_k = 10000000000
for i in range(1,n//2+1):
    sum_k = 0
    a = str(i)
    b = str(n-i)
    for j in a:
        sum_k += int(j)
    for j in b:
        sum_k += int(j)
    min_k = min(min_k,sum_k)
print(min_k)