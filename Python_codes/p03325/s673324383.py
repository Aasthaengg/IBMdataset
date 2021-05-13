N=int(input())
a=list(map(int,input().split()))
sum = 0
for k in a:
    while (k % 2 == 0):
        k = k // 2
        sum += 1
print(sum)