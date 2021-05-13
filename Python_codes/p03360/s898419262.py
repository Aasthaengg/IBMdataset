a, b, c = map(int, input().split())
K = int(input())
max_a = max(a, b, c)
print(sum([a, b, c])-max_a+max_a*(2**K))