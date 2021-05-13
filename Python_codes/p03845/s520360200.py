n = int(input())
t = list(map(int,input().split()))
m = int(input())
d = [list(map(int,input().split())) for i in range(m)]
s = sum(t)
for i in d:
    ans = s - t[i[0]-1] + i[1]
    print(ans)