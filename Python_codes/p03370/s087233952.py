N,X = map(int,input().split())
m = [int(input()) for m in range(N)]
print(N + (X-sum(m))//min(m))