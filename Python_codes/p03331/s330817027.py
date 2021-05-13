#template
def inputlist(): return [int(j) for j in input().split()]
#template
#issueから始める
N = int(input())
def wa(N) : #kakuketanowa
    S = str(N)
    array = list(map(int,S))
    return sum(array)
ans = 10**9+7
for i in range(1,N):
    l = i
    r = N-i
    suma = wa(l) + wa(r)
    ans = min(ans,suma)
print(ans)