n, q = map(int, input().split())
s = input()
lr = [list(map(int, input().split())) for i in range(q)]
t = [0] * (n+1)
for i in range(n):
    t[i+1] = t[i] + (1 if s[i:i+2] == "AC" else 0)
for i in range(q):
    print(t[lr[i][1]-1] - t[lr[i][0]-1])