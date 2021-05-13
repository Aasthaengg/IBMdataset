from math import sqrt, ceil

def tostr(a):
    return ' '.join(map(str, a))

N = int(input())
k = ceil(sqrt(N*2))
#print(k)
if N!=k*(k-1)/2:
    print('No')
    exit()

print('Yes')
print(k)
M = k - 1
# diagonal
a = [1]
for i in range(M-1):
    a.append(a[-1] + i + 2)
print(M, tostr(a))
#
for i in range(M):
    a = [int(i*(i+1)/2) + 1]
    a += list(range(a[-1]+1, a[-1]+i+1))
    #print(a)
    for j in range(i+1, M):
        a.append(a[-1] + j)
    print(M, tostr(a))
        
