N=int(input())
info=[list(map(int,input().split())) for _ in range(N)]
info.sort(key=lambda x:x[0],reverse=True)
print(info[0][0]+info[0][1])

