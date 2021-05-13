N,K = map(int,input().split())
possibility = 0


for i in range(1,N+1):
    count = 0
    point = i
    while(point <= K-1):
        point = point * 2
        count += 1
    possibility += 0.5**count

print(possibility / N)