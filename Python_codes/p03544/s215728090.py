N = int(input())

lis = [2, 1]

for i in range(2, N+1):
    lis.append(lis[i-1]+lis[i-2])

if N == 1:
    print(1)
else:
    print(lis[N])
