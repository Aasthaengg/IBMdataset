(N, A, B) = map(int, input().split())
answer = 0
for i in range(N):
    sumdig = 0
    for j in str(i + 1):
        sumdig += int(j)
    if A <= sumdig and sumdig <= B:
        answer += i + 1
print(answer)
