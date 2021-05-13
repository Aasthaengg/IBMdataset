## C - Candies
N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
candy = []
for n in range(N):
    candy.append(sum(A1[:n+1]) + sum(A2[n:]))
print(max(candy))