from bisect import bisect_right
n=int(input())
A=[int(input()) for _ in range(n)][::-1]

DP=[A[0]]
for i in range(1,n):
    num=A[i]
    if num>=DP[-1]:
        DP.append(num)
    else:
        index=bisect_right(DP,num)
        DP[index]=num
print(len(DP))