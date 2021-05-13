N = int(input())

Flag = [False]*(N+1)
Flag[0] = True

num = 3
while num <= N:
    Flag[num] = True
    num += 3

num = 5
while num <= N:
    Flag[num] = True
    num += 5

count = 0
for f in range(1, N+1):
    if Flag[f] == False:
        count += f

print(count)