n = int(input())
list = []

for _ in range(n):
    list.append(int(input()))

print(len(set(list)))