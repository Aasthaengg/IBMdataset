import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

a,b = li()
grid = []
for i in range(100):
    if i < 50:
        grid.append(["."]*100)
    else:
        grid.append(["#"]*100)
                     
for i in range(b-1):
    grid[i//25][2*(i%50)] = "#"

    
for j in range(a-1):
    grid[(-j-1)//25][2*(j%50)] = "."
    
    
print(100, 100)
for i in range(100):
    print("".join(grid[i]))