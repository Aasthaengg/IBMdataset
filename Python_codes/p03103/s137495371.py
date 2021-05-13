N,M=map(int,input().strip().split())
AB=[list(map(int,input().strip().split())) for _ in range(N)]
AB.sort()

num=0
money=0
i=0
while num<M:
    num+=AB[i][1]
    money+=AB[i][0]*AB[i][1]
    if i<N-1 and num<M:
    	i+=1

money+=AB[i][0]*(M-num)

print(money)