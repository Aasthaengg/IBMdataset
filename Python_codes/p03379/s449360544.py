n = int(input())
x = list(map(int,input().split()))
y = sorted(x)
med_small = y[n//2-1]
med_large = y[n//2]
for i in range(n):
    if x[i] <= med_small:
        print(med_large)
    else:
        print(med_small)