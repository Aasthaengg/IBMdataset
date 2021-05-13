n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

sa =0
ea = 0

for i in range(n):
    sa +=ab[i][0]
    ea +=ab[i][1]
    
print(ea-sa+n)