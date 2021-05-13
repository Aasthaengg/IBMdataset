#ABC073

n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
r = [l[i][1] - l[i][0] + 1 for i in range(n)]

print(sum(r))

