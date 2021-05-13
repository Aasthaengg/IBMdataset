N = int(input())
A = list(map(int,input().split()))

f = [i for i in range(N)]
left, right = 0, 0
ans = 0
nowxor = 0
nowsum = 0
for left in range(N):
    while right < N and nowxor ^ A[right] == nowsum + A[right]:
        nowsum += A[right]
        nowxor = nowxor ^ A[right]
        right += 1
    ans += right - left
    if left == right:
        right += 1
    else:
        nowsum -= A[left]
        nowxor = nowxor ^ A[left]
print(ans)