import sys
def input():
  return sys.stdin.readline().rstrip()

def rec(i,a,b,c):
  if i==N:
    if a==0 or b==0 or c==0:
      return 10**12
    return abs(a-A)+abs(b-B)+abs(c-C)

  res=rec(i+1,a,b,c);

  res=min(res,rec(i+1,a+l[i],b,c)+(10 if a else 0))
  res=min(res,rec(i+1,a,b+l[i],c)+(10 if b else 0))
  res=min(res,rec(i+1,a,b,c+l[i])+(10 if c else 0))

  return res

N,A,B,C=map(int,input().split())
l=[int(input()) for _ in range(N)]

print(rec(0,0,0,0))
