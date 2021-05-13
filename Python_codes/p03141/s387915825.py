n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
l.sort(key=lambda x:x[0]+x[1],reverse=True)

print(sum([l[i][0] for i in range(n) if i % 2 == 0]) - sum([l[i][1] for i in range(n) if i % 2 == 1]))