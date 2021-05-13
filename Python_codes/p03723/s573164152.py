A, B, C = map(int, input().split())
count = 0
ABC = []
while True:
    if A % 2 ==0 and B % 2 == 0 and C % 2 == 0:
        nA = B/2 + C/2
        nB = A/2 + C/2
        nC = A/2 + B/2
        A, B, C = nA, nB, nC
        count += 1
        if [A, B, C] in ABC:
            count = -1
            break
        ABC.append([A, B, C])
    else:
        break
print(count)