n, m, k = map(int, input().split())
a_books = list(map(int,input().split()))
b_books = list(map(int,input().split()))
sum1 = [0]
sum2 = [0]
for i in range(n):
 sum1.append(sum1[-1]+a_books[i])
for i in range(m):
 sum2.append(sum2[-1]+b_books[i])
ans=0
import bisect
for i in range(n+1):
    if sum1[i] > k:
        break
    j = bisect.bisect_right(sum2, k-sum1[i])-1
    ans = max(ans, i+j)
print(ans)
