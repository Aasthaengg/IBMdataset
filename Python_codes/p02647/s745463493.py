N, K = map(int, input().split())
A = list(map(int, input().split()))
foo = [[0 for k in range(N)] for k in range(42)]
for k in range(len(A)):
    foo[0][k] = A[k]
if K <42:
    for q in range(K):
        unko = [0 for k in range(N)]
        for k in range(N):
            if k + foo[q][k]+1 < N:
                unko[k + foo[q][k]+1] -=1
            unko[max(k - foo[q][k], 0)] +=1
        unchi = 0
        for k in range(N):
            unchi += unko[k]
            foo[q+1][k] = unchi
        #print(unko)
        #print(foo[q+1])
        count =0
        for l in range(N):
            if foo[q+1][l] < N:
                break
            else:
                count +=1
        
        if count == N:
            break
        
                        
        #print(foo)
    print(" ".join(map(str, foo[q+1])))

     
else:
    print((str(N)+" ")*(N-1)+str(N))


