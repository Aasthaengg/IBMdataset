n = int(input())

a = [list(map(int,input().split())) for i in range(2)]

total = 0
st_num = 0
max_num = 0
for i in range(n):
    st_num += a[0][i]
    for j in range(i,n):
        total += a[1][j]
    if max_num < st_num+total:
        max_num = st_num+total
    total = 0
print(max_num)