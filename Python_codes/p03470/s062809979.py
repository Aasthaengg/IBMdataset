n = int(input())

mochies = []
cnt = 0
for i in range(n):
    mochies.append(int(input()))

print(len(set(mochies)))