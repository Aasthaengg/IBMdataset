n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
D = {}
for i in range(n):
    if d[i] not in D:
        D[d[i]] = 1
    else:
        D[d[i]] += 1
T = {}
for j in range(m):
    if t[j] not in T:
        T[t[j]] = 1
    else:
        T[t[j]] += 1
for k in T:
    try:
        if T[k] <= D[k]:
            continue
        else:
            print('NO')
            break
    except:
        print('NO')
        break
else:
    print('YES')
