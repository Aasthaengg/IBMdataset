S = input()
T = input()
count = [i for i, j in zip(T, S) if i == j]
print(len(count))