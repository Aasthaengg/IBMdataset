n = map(int, input().split())
t = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for _ in range(m)]

ans = sum(t)
for p,x in px:
    a = ans-t[p-1]+x
    print(a)