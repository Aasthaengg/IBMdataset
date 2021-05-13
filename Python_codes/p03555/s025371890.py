C1 = list(str(input()))
C2 = list(str(input()))[::-1]

for i in range(3):
    if not C1[i]==C2[i]:
        print('NO')
        break
else:
    print('YES')