n = int(input())
lis = [list(map(int,input().split())) for i in range(n)]
print(sum([lis[i][1]-lis[i][0]+1 for i in range(n)]))