N = int(input())
ABC = [list(input()) for _ in range(3)]

print(sum([len(set(abc)) - 1 for abc in zip(*ABC)]))