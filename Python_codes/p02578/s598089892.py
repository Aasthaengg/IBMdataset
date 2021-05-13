from sys import stdin
def ip(): return [int(i) for i in stdin.readline().split()]
def sp(): return [str(i) for i in stdin.readline().split()]


n = int(input())
A = ip()
k = A[0]
ans = 0
for i in range(len(A)):
    k = max(k, A[i])
    ans += (k - A[i])
print(ans)
