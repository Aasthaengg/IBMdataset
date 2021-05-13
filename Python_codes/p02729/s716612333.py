N, M = map(int, input().split())
l = ['e'] * N + ['o'] * M
cnt = 0
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        if l[i] != l[j]:
            pass
        else:
            cnt += 1
print(cnt)