N = int(input())

cnt = 0
A = []
for u in range(1, N) :
    for v in range(u+1, N+1) :
        if u + v == N + (N % 2 != 1) :
            continue
        else :
            cnt += 1
            A.append((u, v))

print(cnt)
for i in range(cnt) :
    print(*A[i])
