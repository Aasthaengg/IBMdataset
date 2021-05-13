N = int(input())
A = list(map(int, input().split()))
l, r, fl, fr, gl, gr, ans= 0, 0, 0, A[0], 0, A[0], 0
while l < N:
    while r+1 < N and fr-fl+A[r+1] == gr^gl^A[r+1]:
        r += 1
        fr += A[r]
        gr ^= A[r]
    ans += r-l+1
    fl += A[l]
    gl ^= A[l]
    l += 1
print(ans)
