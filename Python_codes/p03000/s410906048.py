N, X = map(int, input().split())
L = list(map(int, input().split()))

coordinate = 0
count = 0

while count < N:
    coordinate += L[count]
    if coordinate > X:
        break
    else:
        count += 1

print(count+1)
