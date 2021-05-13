n, q = map(int, input().split())
s = input()
LR = [list(map(int, input().split())) for _ in range(q)]

t = [0]*(n+1)

for i in range(n):
    t[i+1] = t[i] + (1 if s[i:i+2]=="AC" else 0)

for i in LR:
    l, r = i[0], i[1]
    print(t[r-1] - t[l-1])