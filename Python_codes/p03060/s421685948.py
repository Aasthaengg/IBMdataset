input()
f=lambda:map(int,input().split())
print(sum(max(x-y,0) for x,y in zip(f(),f())))