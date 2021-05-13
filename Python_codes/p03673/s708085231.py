N=int(input())
A=list(map(int, input().split()))
even = [A[i] for i in range(0, N, 2)]
odd = [A[i] for i in range(1, N, 2)]
if N%2==0:
    ans = odd[::-1] + even
else:
    ans = even[::-1] + odd
print(*ans)