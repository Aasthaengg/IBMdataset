N, K = map(eval, input().split())
candy = []

for i in range(K):
    input()
    candy.append(list(map(eval, input().split())))

result = 0

for i in range(1, N+1):
    for j in range(K):
        if i in candy[j]:
            break
    else:
        result += 1

print(result)