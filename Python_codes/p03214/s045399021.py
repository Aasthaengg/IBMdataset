N = int(input())
*A, = map(int, input().split())

ave = 0
for i in range(len(A)):
    ave = ave + A[i]
ave = ave / N

min = float("inf")
for i in range(len(A)):
    temp = abs(A[i]-ave)

    if min> temp:
        min = temp
        ans = i
print(ans)