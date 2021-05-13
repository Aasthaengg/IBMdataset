import itertools

N = int(input())

A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))

#どこで下の行に移るか
csA1 = list(itertools.accumulate(A1))
csA2 = list(itertools.accumulate(A2))

#print(csA1)
#print(csA2)

ans = A1[0] + csA2[-1]
for i in range(N-1):
    tmp = csA1[i] + (csA2[-1] - csA2[i]) + A2[i]
    ans = max(ans,tmp)
print(ans)