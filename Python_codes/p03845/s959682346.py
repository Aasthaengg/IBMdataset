n = int(input())
t_li = list(map(int,input().split()))
m = int(input())
d_li=[list(map(int,input().split())) for i in range(m)]

time = sum(t_li)

for i, j in d_li:
    print(time - t_li[i-1] + j)