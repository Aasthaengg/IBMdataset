n, C = map(int, input().split())
pro = [list(map(int, input().split())) for i in range(n)]

time = [0 for _ in range(2*10**5 + 2)]

for i in range(C):
    w = [0 for _ in range(2*10**5 + 2)]
    for s,t,c in pro:
        if c == i + 1:
            w[2*s-1] += 1
            w[2*t] -= 1
    for j in range(2*10**5+1):
        w[j+1] += w[j]
        if w[j+1]:
            time[j+1] += 1

print(max(time))
