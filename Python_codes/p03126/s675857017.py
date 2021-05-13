N, M = map(int, input().split())
dic = {i :0 for i in range(1, M+1)}

for j in range(N):
    lis = list(map(int, input().split()))
    count = lis[0]
    answer = lis[1:]
    for k in answer:
        dic[k] += 1

num = [x for x in dic.values() if x == N]
print(len(num))

