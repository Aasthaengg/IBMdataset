A,B,T = map(int,input().split())

res = 0
cnt = 0
t = T + 0.5

loop = T // A

for i in range(loop):
    if(cnt <= t):
        res += B
        cnt = i * A
    else:
        break
print(res)
