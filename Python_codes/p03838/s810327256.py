x,y=list(map(int,input().split()))
def f(s):
   if s < 0:
      return 10**10
   else:
      return s
print(min(f(y-x),f(-y+x)+2,f(y+x)+1,f(-y-x)+1))