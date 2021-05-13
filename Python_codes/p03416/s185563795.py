A, B = map(int, input().split())
count = 0
while A <= B:
    n = str(A)
    if n[0] == n[-1] and n[1] == n[-2]:
        count += 1
    A += 1
print(count)