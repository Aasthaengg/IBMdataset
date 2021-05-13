n,m = map(int,input().split())
li=[list(map(int,input().split())) for i in range(m)]
ans_li = [0] * n

for i, j in li:
    ans_li[i-1] += 1
    ans_li[j-1] += 1

print(*ans_li,sep="\n")