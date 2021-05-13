X,Y,A,B,C = map(int,input().split())
r = sorted(list(map(int,input().split())),reverse=True)[:X]
g = sorted(list(map(int,input().split())),reverse=True)[:Y]
w = list(map(int,input().split()))

new = sorted(r+g+w,reverse=True)
print(sum(new[:X+Y]))