N = int(input())
A = [int(x) for x in input().split()]
i = 0
money = 1000
while i < N-1:
    today = i
    j = i + 1
    while A[i] <= A[j]:
        i += 1; j += 1
        if j == N:
            break
    money += (money // A[today]) * (A[i] - A[today])
    i = j
print(money)