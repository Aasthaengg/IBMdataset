n = int(input())
ab = [list(map(int,input().split())) for i in range(n)]
ab = sorted(ab, key=lambda x:(x[1], x[0]))

t = 0
for i in range(n):
    t += ab[i][0]
    if t > ab[i][1]:
        print('No')
        exit()
print('Yes')