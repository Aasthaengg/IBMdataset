N,X = map(int,input().split())
m = [int(input()) for _ in range(N)]

count = N
count += (X-sum(m))//min(m)

print(count)