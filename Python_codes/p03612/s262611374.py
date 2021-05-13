N = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if p[i] == i+1:
        if i != N-1:
            temp = p[i]
            p[i] = p[i+1]
            p[i+1] = temp
            cnt += 1
        else:
            cnt += 1
print(cnt)