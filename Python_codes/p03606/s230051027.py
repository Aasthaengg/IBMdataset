n = int(input())
l = [list(map(int, input().strip().split())) for i in range(n)]
cnt = 0
for i in l:
    cnt += len([j for j in range(i[0], i[1]+1)])
print(cnt)