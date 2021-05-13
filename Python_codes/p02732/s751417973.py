import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

nn = int(input())
aa = list(map(int,input().split()))

ne = [0]*(nn+1)
cn = [0]*(nn+1)
cnminus1 = [0]*(nn+1)
#print(nn,aa)
#print(len(ne))
for i in range(nn):
    ne[aa[i]] += 1

for i in range(nn+1):
 #   print(ne[i])
    if ne[i] == 0:
        cn[i] = 0
        cnminus1[i] = 0
    elif ne[i] == 1:
        cn[i] = 0
        cnminus1[i] = 0
    elif ne[i] == 2:
        cn[i] = 1
        cnminus1[i] = 0
    else:
        cn[i] = combinations_count(ne[i],2)
        cnminus1[i] = combinations_count(ne[i]-1,2)

sum_cn = sum(cn)

for i in range(nn):
    print(sum_cn - cn[aa[i]] + cnminus1[aa[i]])

