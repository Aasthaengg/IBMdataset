N, K = map(int, input().split())
S = input()

arr =[]
for i in range(N):
    if i+1 == K:
        arr.append(str.lower(S[i]))
    else:
        arr.append((S[i]))

print(*arr, sep='')

