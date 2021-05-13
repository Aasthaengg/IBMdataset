N,T = map(int, input().split())
tl = list(map(int, input().split()))
answer = 0
for i in range(N):
    if i == 0:
        answer = T
    else:
        if tl[i] - tl[i-1] >= T:
            answer += T
        else:
            answer += tl[i] - tl[i-1]
print(answer)