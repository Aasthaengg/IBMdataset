n = int(input())
b = list(map(int, input().split()))
procedure = [-1] * n
tmp_n = n
for m in range(n-1, -1, -1):
    for i in range(tmp_n-1, -1, -1):
        if b[i] == i+1:
            procedure[m] = i + 1
            del b[i]
            tmp_n -= 1
            break
    else:
        print(-1)
        exit()
for i in range(n):
    print(procedure[i])
