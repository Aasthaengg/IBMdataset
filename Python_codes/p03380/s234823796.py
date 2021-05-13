n = int(input())
A = list(map(int, input().split()))
AS = sorted(list(set(A)))
n = AS[-1]
checkAS = len(AS)-1
nHalf = n/2
min = 10**10


for i in range(checkAS):
    temp = abs(AS[i]-nHalf)
    if min > temp:
        r = AS[i]
        min = temp

print(str(n) + ' ' + str(r))