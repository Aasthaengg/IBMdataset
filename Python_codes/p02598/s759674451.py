#template
def inputlist(): return [int(j) for j in input().split()]
#template
N,K = inputlist()
A = inputlist()
left = 0
right = 10**9+1
while right - left > 1:
    mid = (left+right)//2
    count = 0
    for i in range(N):
        count += A[i]//mid
        if A[i] % mid == 0:
            count -=1
    if count > K:
        left = mid
    else:
        right = mid
print(right)
