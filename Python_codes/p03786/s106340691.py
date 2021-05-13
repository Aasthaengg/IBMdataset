N = int(input())
A = list(map(int,input().split()))
A.sort()
cums = [0]
for i in range(N):
    cums.append(cums[-1] + A[i])
#print(A)
cums.pop(0)
#print(cums)
ans = 1
for i in range(N-2,-1,-1):
    if A[i+1] <= 2*cums[i]:
        #print(A[i])
        ans += 1
    else:
        print(ans)
        exit()
print(ans)