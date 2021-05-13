#!/usr/bin.env python3

N,K = map(int,input().split())
queries = [list(map(int,input().split())) for _ in range(N)]

queries = sorted(queries,key=lambda x: x[0])

arrayLength = 0
for i in range(N):
  arrayLength += queries[i][1]
  if arrayLength >= K:
    print(queries[i][0])
    exit()
print(-1)
