N = int(input())
li = [list(map(int,input().split())) for _ in range(2)]
ma = 0
for i in range(N):
    li1 = li[0][0:i+1]
    li2 = li[1][i::]
    if ma <= sum(li1)+sum(li2):
        ma = sum(li1)+sum(li2)
print(ma)