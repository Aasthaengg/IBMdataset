N,X = map(int,input().split())
ml = [int(input()) for _ in range(N)]

add = (X-sum(ml))//min(ml)
print(N+add)