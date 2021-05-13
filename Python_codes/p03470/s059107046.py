n = int(input())

mochies = []
cnt = 0
for i in range(n):
    mochies.append(int(input()))

print(sum([min(set(mochies)) < i for i in set(mochies)])+1)