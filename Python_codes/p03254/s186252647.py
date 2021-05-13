N, x = map(int, input().split())

A = list(map(int, input().split()))

count = 0

while(len(A)) != 1:
    x -= min(A)
    if x < 0:
        break
    A.remove(min(A))
    count += 1
    if len(A) == 1:
        if x - min(A) == 0:
            count += 1

print(count)