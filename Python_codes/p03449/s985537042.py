N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))

candies = []

for i in range(N):
    candies.append(sum(A1[:i+1])+sum(A2[i:]))
print(max(candies))
