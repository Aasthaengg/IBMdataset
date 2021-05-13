n, k = map(int, input().split())


A = [i for i in range(n+1)]
left = [A[0]]
right = [0 for i in range(n+1)]
right[-1] = A[-1]
for i in range(1, n+1):
    left.append(left[i-1] + A[i])
for i in range(n-1, -1, -1):
    right[i] = right[i+1]+A[i]
#print (left, right)
ans = 0
M = 10**9+7
for i in range(k, n+2):
    #print (ans, A[:i], A[n+1-i:])
    ans = (ans + right[-i]) % (10**9+7)
    #print (ans, right[-i], left[i-1]-1)
    #print (left[i-1])
    #print (ans - left[i-1]+1)
    ans = (ans - left[i-1]+1) % (10**9+7)
print (ans)