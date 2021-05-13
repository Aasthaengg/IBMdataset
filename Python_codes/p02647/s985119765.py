#coding; utf-8
import copy
N, k = map(int,input().split())
A = list(map(int,input().split()))
B = [0] * N
A = [0] + A
#B = copy.copy(A)
#k = 10
for j in range(k):
    #print(A)
    n_light = [0] * (N+1)
    for i in range(N):
        d = A[i+1]
        l = i+1-d
        r = i+1+d
        #print(l, r)
        n_light[max(l, 1)] += 1
        if r+1 <= N:# and l != r:
            n_light[r+1] -= 1
        #print(n_light)
    #print(n_light)
    for i in range(1,N):
        n_light[i+1] += n_light[i]
    n_str = [str(i) for i in n_light]
    if len(set(n_light[1:])) == 1 and j > 2:
        #print(n_light)
        break
    #n_str = [str(i) for i in n_light]
    A = n_light
    #print(n_light) 
print(' '.join(n_str[1:]))
    
