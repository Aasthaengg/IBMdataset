N = int(input())
A = list(map(int,input().split()))
MAX = max(A)
BIG = 10**9+7
L = len(bin(MAX)[2:])
ans = 0
for j in range(L):
    zero = 0
    one = 0
    for i in range(N):
        if (A[i] >> j) & 1:
            one+=1
        else:
            zero+=1
    ans += ((zero*one)%BIG)*pow(2,j,BIG)
    ans = ans%BIG
print(ans)