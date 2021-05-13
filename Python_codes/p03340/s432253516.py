N = int(input())
A = list(map(int,input().split()))

xorsum = A[0]
right = 0
ans = 0
for left in range(N):
    if right < N-1:
        while xorsum+A[right+1]==xorsum^A[right+1]:
            right += 1
            xorsum += A[right]
            if right == N-1:
                break
        xorsum -= A[left]
    ans += right-left+1
    
print(ans)