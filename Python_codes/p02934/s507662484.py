a = int(input())
b = list(map(int, input().split()))
j = [1 / i for i in b]
print(1 / sum(j))