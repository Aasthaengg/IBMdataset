import sys
input = sys.stdin.buffer.readline

n,A,B,C = map(int,input().split())
L = []
for _ in range(n):
    L.append(int(input()))

res = 10**9

for i in range(4**n):
    flag = i
    a,b,c,tmp = 0,0,0,0
    for j in range(n):
        flag,now = divmod(flag,4)
        if now == 1:
            if a != 0:
                tmp += 10
            a += L[j]
        elif now == 2:
            if b != 0:
                tmp += 10
            b += L[j]
        elif now == 3:
            if c != 0:
                tmp += 10
            c += L[j]
    if a*b*c == 0:
        continue

    tmp += abs(A-a) + abs(B-b) + abs(C-c)

    res = min(res,tmp)

print(res)