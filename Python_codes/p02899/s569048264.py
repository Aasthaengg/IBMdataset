from operator import itemgetter
N = int(input())
A = list(map(int, input().split()))
# a= []
# for i in range(N):
#     a.append((i+1, A[i]))
#     a.sort(key=itemgetter(1))
# print(' '.join([str(i[0]) for i in a]))
a = [0] * N
for i in range(N):
    a[ A[i] -1 ] = str(i + 1)
print(' '.join(a))
