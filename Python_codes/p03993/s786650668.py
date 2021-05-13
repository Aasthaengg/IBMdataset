n = int(input())
l = [False] * n
inputList = list(map(int, input().split()))
pairs = 0
for i in range(n):
    if l[i]:
        continue

    x = inputList[i]-1 
    if inputList[x]-1 == i:
        pairs += 1
        l[x] = True
print(pairs)