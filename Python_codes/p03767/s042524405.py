N = int(input())

a = list(map(int, input().split()))

a = sorted(a, reverse=True)



SUM = 0

for i in range(1, N*2, 2):
    
    SUM = SUM + a[i]

print(SUM)