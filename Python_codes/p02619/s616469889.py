#B
D = int(input())
c = [0] + list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]

last = [0] * 27
manzoku = [0] * 27
for i in range(1, D+1):
    t = int(input())
    manzoku[t] += s[i-1][t-1]
    last[t] = i
    for j in range(1, 27):
        manzoku[j] -= c[j] * (i - last[j])
            
    result = 0
    for k in range(27):
        result += manzoku[k]
    print(result)
