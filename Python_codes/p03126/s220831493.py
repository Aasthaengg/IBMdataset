N, M = map(int, input().split())
a = [set(input().split()[1:]) for _ in range(N)]
 
like = a[0]
for i in range(1, N):
    like = like & a[i]
print(len(like))