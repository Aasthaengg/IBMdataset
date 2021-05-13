#template
def inputlist(): return [int(j) for j in input().split()]
def listinput(): return input().split()
#template
N = int(input())
X = inputlist()
ans = 10**9+7
for i in range(101):
    tmp = 0
    for j in range(N):
        tmp += (X[j]- i)**2
    ans = min(ans,tmp)
print(ans)