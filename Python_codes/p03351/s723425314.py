A, B, C, D = map(int, input().split())
ABC = [A,B,C]
if abs(ABC[0] - ABC[2]) <= D:
    print('Yes')
    exit(0)
for i in range(1,3):
    if abs(ABC[i] - ABC[i-1]) <= D:
        continue
    else:
        print('No')
        exit(0)
print('Yes')

