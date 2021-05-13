n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
b=[y for x,y in ab]
c=[x+y for x,y in ab]
c.sort(reverse=True)
print(sum(c[::2])-sum(b))