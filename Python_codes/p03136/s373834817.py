#ABC117 B:Polygon

N = int(input())
l = [int(i) for i in input().split()]
ans = 'No'
#l = list(map(int,input().split()))

ma = max(l)
su = sum(l) - ma

if su > ma:
    ans ='Yes'
print(ans)
