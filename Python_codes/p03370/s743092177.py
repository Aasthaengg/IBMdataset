n,x = map(int,input().split())
mini = 10**5
for i in range(n):
    m = int(input())
    x -= m
    mini = min(mini,m)
print(n + x//mini)