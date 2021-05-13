n=[[i+1,input().split()] for i in range(int(input()))]
[print(i[0]) for i in sorted(n,key=lambda x:(x[1][0],-int(x[1][1])))]