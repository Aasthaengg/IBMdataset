N = int(input())
A = list(map(int,input().split()))

Alist = [A[i]-(i+1) for i in range(N)]
Alist.sort()
x = N//2
b = Alist[x]
ans = 0
for i in range(N) :
    ans += abs(Alist[i]-b)
    
print(ans)