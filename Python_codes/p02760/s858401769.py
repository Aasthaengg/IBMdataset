A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
N = int(input())
lst = []
for _ in range(N):
    i = int(input())
    lst.append(i)

for n, i in enumerate(A1):
    for j in lst:
        if i == j:
            A1[n] = 0

for n, i in enumerate(A2):
    for j in lst:
        if i == j:
            A2[n] = 0
            
for n, i in enumerate(A3):
    for j in lst:
        if i == j:
            A3[n] = 0
            
B1 = sum(A1)
B2 = sum(A2)
B3 = sum(A3)
B4 = A1[0] + A2[0] + A3[0]
B5 = A1[1] + A2[1] + A3[1]
B6 = A1[2] + A2[2] + A3[2]
B7 = A1[0] + A2[1] + A3[2]
B8 = A1[2] + A2[1] + A3[0]

if B1 * B2 * B3 * B4 * B5 * B6 * B7 * B7 * B8 == 0:
    print('Yes')
else:
    print('No')