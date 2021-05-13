from collections import Counter

N = int(input())
A = list(map(int, input().split()))

count = [0]*(N+1)

for a in A:
    count[a] += 1

sum_ = sum(map(lambda x: int(x*(x-1)/2), count))

ans = []

for a in A:
    temp = sum_ - (count[a] - 1)
    ans.append(temp)

print(*ans, sep='\n')
