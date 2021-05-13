n = int(input())
li = [list(map(int,input().split())) for _ in range(2)]

ma = 0

for i in range(n):
    ma = max(ma,sum(li[0][:i+1])+sum(li[1][i:]))

print(ma)