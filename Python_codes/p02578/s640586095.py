#template
def inputlist(): return [int(j) for j in input().split()]
#template
N = int(input())
A = inputlist()
maxa = A[0]
ans= 0
for i in range(1,N):
    if A[i] < maxa:
        ans += maxa - A[i]
    else:
        maxa = A[i]
print(ans)