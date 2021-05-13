N=int(input())
n=[list(map(int,input().split())) for _ in range(N)]
print(sum([max(i)-min(i)+1 for i in n]))