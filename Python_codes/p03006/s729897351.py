from collections import deque
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

d = dict()
for point in xy:
    d[str(point)] = 1


if N == 1:
    print(1)
    exit()

ans = N
que = deque()

for i in range(N):
    for j in range(i+1, N):
        p = xy[i][0] - xy[j][0]
        q = xy[i][1] - xy[j][1]

        ans_tmp = N

        for point in xy:
            add = [point[0] + p, point[1] + q]
            # sub = [point[0] - p, point[1] - q]
            if d.get(str(add)) == 1:
                ans_tmp -= 1
                d[str(add)] -= 1
                que.append(str(add))
            # if d.get(str(sub)) == 1:
            #     ans -= 1
            #     d[str(sub)] -= 1
        
        ans = min(ans, ans_tmp)
        
        while len(que):
            key = que.pop()
            d[key] += 1
        


print(ans)


