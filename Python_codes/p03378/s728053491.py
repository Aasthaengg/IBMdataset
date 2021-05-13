N, M, X = map(int, input().split())
a = list(map(int, input().split()))

count = [i for i in a if i > X]
print(min(len(count), len(a)-len(count)))
