n = int(input())

info = [list(map(int,input().split())) for _ in range(n)]

max_value = 0
point = 10**10

for i in range(n):
    if info[i][0] > max_value:
        max_value = info[i][0]
        point = info[i][1]
        
print(max_value + point)