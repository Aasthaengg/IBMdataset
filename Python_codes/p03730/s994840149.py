A, B, C = map(int, input().split())

for n in range(100):
    if (B*n+C)%A==0:
        print('YES')
        exit()
    else:
        continue
print('NO')