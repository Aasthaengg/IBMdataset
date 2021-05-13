N=int(input())
lr=[list(map(int,input().split())) for _ in range(N)]
print(sum([e[1]-e[0]+1 for e in lr]))
