n = int(input())
ls = list(map(int,input().split()))
mx = sum(ls)
a = 0
k = float("inf")
for i in range(n-1):
    a += ls[i]
    if k > abs(mx-a*2):
        k = abs(mx -a*2)
print(k)
