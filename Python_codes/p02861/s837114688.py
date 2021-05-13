import itertools
n = int(input())
points = [ list(map(int,input().split())) for _ in range(n)]
routes = list(itertools.permutations(points))
ans = 0
for route in routes:
    for i in range(len(route)-1):
        x,y = route[i][0],route[i][1]
        a,b = route[i+1][0],route[i+1][1]
        ans += ((x-a)**2+(y-b)**2 )**(0.5)
ans /= len(routes)        
print(ans)