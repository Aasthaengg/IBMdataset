N = int(input())
def length(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)
p = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        ans += length(p[i],p[j])
print(ans*2/N)