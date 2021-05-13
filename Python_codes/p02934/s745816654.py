N = int(input())
A = list(map(int, input().split()))
result = [1/i for i in A]
result = 1 / sum(result)
print(result)