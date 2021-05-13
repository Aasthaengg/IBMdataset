N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
candies = [sum(A1[:i+1] + A2[i:]) for i in range(N)]
print(max(candies))