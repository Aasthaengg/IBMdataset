N = int(input())
A = list(map(int, input().split()))

money = 1000;stack=0

for i in range(N-1):
    if A[i]<A[i+1]:
        stack+=money//A[i]
        money %= A[i]
    elif A[i]>A[i+1]:
        money += stack*A[i]
        stack=0

money += stack*A[N-1]
stack=0

print(money)
