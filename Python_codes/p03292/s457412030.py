a = sorted(list(map(int, input().split())))
c = 0
for i in range(1, 3):
    c += abs(a[i]-a[i-1]) 
print(c)