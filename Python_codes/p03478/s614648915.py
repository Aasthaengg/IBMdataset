N, A, B = map(int, input().split())

cnt = []
for i in range(1, N+1):
    if A <= sum(map(int,str(i))) <= B:
        cnt += [i]
print(sum(cnt))
