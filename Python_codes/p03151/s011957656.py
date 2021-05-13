import bisect
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
sumA = sum(A)
sumB = sum(B)
if sumA<sumB:exit(print(-1))
surplus = [0]*n
for i in range(n):
    surplus[i] = A[i]-B[i]
surplus.sort()

index_zero = bisect.bisect_left(surplus,0)
reqt = sum(surplus[:index_zero])
ans = index_zero
index_ = n-1
#print(surplus, index_zero, reqt)
while reqt < 0:
    reqt += surplus[index_]
    index_ -= 1
    ans += 1
print(ans)
