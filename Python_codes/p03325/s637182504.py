def d(x,c):
 if x%2!=0: return c
 return d(x/2, c+1)

input()
print(sum(d(i,0) for i in map(int,input().split())))