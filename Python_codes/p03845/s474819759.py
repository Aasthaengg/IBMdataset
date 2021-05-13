n = int(input())
t = list(map(int, input().split()))
m = int(input())
p = [list(map(int, input().split())) for _ in range(m)]
a = sum(t)
for i,j in p:
    print(a-t[i-1]+j)