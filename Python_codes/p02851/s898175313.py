N,K = map(int,input().split())
A = list(map(int,input().split()))

import copy
B = copy.deepcopy(A)
for i in range(N):
    B[i] -= 1

C = [0]
for i in range(N):
    C.append((C[-1]+B[i])%K)

from collections import defaultdict
D = defaultdict(list)
for i in range(N+1):
    D[C[i]].append(i)

ans = 0
#print(B)
#print(C)
#print(D)
for i in D:
    E = D[i]
    #print(ans)
    if len(E)>=2:
        left = 0
        right = 1
        count = 0
        flag = 0
        while left != len(E)-1 :
            if E[right]-E[left] < K:
                if right == len(E)-1:
                    if flag == 0:
                        count += 1
                        flag = 1
                    ans += count
                    left += 1
                    count -= 1
                else:
                    count += 1
                    right += 1
            else:
                ans += count
                count -= 1
                left += 1
print(ans)