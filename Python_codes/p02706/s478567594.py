N, M = map(int, input().split()) 
A = list(map(int, input().split()))
 
# N-sum(A)が残り日数である
s = sum(A)
ans = -1
if N >= s: ans = N - s
print(ans)