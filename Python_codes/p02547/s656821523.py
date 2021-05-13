N = int(input())
point = 0
for i in range(N):
    D1, D2 = map(int, input().split())
    if D1 == D2:
        point += 1
    else:
        point = 0
    if point == 3:
        print('Yes')
        exit()
print('No')
