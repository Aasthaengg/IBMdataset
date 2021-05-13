x,y = map(int,input().split())

f = lambda x,y: y-x if y >= x else float('inf')

print(min(f(x,y), 1+f(-x,y), 2+f(-x,-y), 1+f(x,-y)))