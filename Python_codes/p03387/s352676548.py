A = list(map(int, input().split()))
A.sort()
Ans = 0
temp = (A[2] - A[0])//2
Ans += temp
A[0] += temp*2
temp = (A[2] - A[1])//2
Ans += temp
A[1] += temp*2
if A[0] == A[1] == A[2]:
    print(Ans)
elif A[0] == A[1]:
    print(Ans+1)
else:
    print(Ans+2)