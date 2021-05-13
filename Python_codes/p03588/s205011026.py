def I(): return int(input())
def LI(): return list(map(int,input().split()))
N = I()
AB = [LI() for _ in range(N)]
ans,max = 0,0
for x in AB:
    a,b = x[0],x[1]
    if a>max:
        max = a
        ans = a+b
print(ans)
