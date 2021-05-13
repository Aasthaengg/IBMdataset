K = int(input())
A = [int(a) for a in input().split()]
    
if A[K-1] == 2:
    l = 2
    r = 2
    flag = True
    for i in range(K-2, -1, -1):
        r += A[i+1]-1
        if l%A[i] > 0:
            l += A[i]-(l%A[i])
        r -= r%A[i]
        if r < l:
            flag = False
            break
    if flag:
        r += A[0]-1
        ans = str(l) + " " + str(r)
    else:
        ans = -1
else:
    ans = -1

print(ans)