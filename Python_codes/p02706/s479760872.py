n, m = map(int, input().split())
A = list(map(int, input().split()))

d = 0
flag = True
for a in A:
    d += a

    if(d > n):
        flag = False
        break

print(n-d if flag else -1)