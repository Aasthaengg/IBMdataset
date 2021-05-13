import bisect

def cin():  return list(map(int,input().split()))

N, M = cin()
l1 = [[] for i in range(N + 1)]
l2 = []
for i in range(M):
    in1, in2 = cin()
    l1[in1].append(in2)
    l2.append([in1, in2])

for i in range(N + 1):  l1[i] = sorted(l1[i])
    
for i in range(M):
    c = l2[i]
    n = bisect.bisect_left(l1[c[0]], c[1]) + 1
    ans = str(c[0]).zfill(6) + str(n).zfill(6)
    print(ans)