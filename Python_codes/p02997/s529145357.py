N,K = map(int, input().split())

if K > (N-1)*(N-2)//2:
    print(-1)
else:
    L = []
    for i in range(N-1):
        L.append(["1", str(i+2)])
    k = (N-1)*(N-2)//2 - K
    i = 2
    j = 3
    while k > 0:
        L.append([str(i), str(j)])
        j += 1
        if j == N+1:
            i += 1
            j = i+1
        k -= 1
        
    print(len(L))
    for i in range(len(L)):
        print(" ".join(L[i]))