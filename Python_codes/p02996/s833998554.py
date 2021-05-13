from operator import itemgetter
N = int(input())
T = []
for _ in range(N):
    T.append(tuple(map(int, input().split())))
T.sort(key=itemgetter(1))
A = [i[0] for i in T]
B = [i[1] for i in T]
sum = 0
for i in range(N):
    sum += A[i]
    if sum > B[i]:
        print('No')
        exit()
print('Yes')
