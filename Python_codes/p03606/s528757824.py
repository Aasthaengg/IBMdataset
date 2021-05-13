n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

res = 0

for i in range(n):
    res += s[i][1] - s[i][0] +1
    
print(res)