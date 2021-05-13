N = int(input())
K = int(input())
x = list(map(int, input().split()))

result = sum([min(K-i, i)*2 for i in x])
print(result)