n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)
sum_a = 0
for i in range(1,2*n+1,2):
    sum_a += a[i]
print(sum_a)