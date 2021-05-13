n = int(input())
A = list(map(int, input().split()))

ans = 1
sq = 0
a = A[0]
for i in range(1,n):
    #print(a,A[i], sq)
    if sq == 0 and A[i] < a:
        sq = -1
    elif sq == 0 and A[i] > a:
        sq = 1
    elif (sq == 1 and A[i] < a) or (sq == -1 and A[i] > a):
        #print('---')
        ans += 1
        sq = 0
    a = A[i]

print(ans)

