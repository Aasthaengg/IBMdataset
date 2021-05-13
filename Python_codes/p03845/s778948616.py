n = int(input())
t = list(map(int, input().split()))
m = int(input())
time = [0] * m
for i in range(m) :
    p, x = map(int, input().split())
    tmp = t[p-1]
    t[p-1] = x
    print(sum(t))
    t[p-1] = tmp
