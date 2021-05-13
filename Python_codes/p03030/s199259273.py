N = int(input())

m = [0]*N

for i in range(N):
    k, v = input().split()
    m[i] = [k, int(v), i+1]

m.sort()

for j in range(N):
    for i in range(N-1):
        if m[i][0] == m[i+1][0] and m[i][1] < m[i+1][1]:
            m[i], m[i+1] = m[i+1], m[i]


for i in m:
    print(i[2])
