n,m=map(int,input().split())
INF=float('inf')
G=[]
for _ in range(m):
  a,b,c=map(int,input().split())
  G.append([a-1,b-1,-c])
  
def main():
  D=[INF for _ in range(n)]
  D[0]=0
  for i in range(n):
    for x,y,z in G:
      if D[x]!=INF and D[y]>D[x]+z:
        D[y]=D[x]+z
        if i==n-1 and y==n-1:
          return 'inf'
  return -D[n-1]
   
if __name__=='__main__':
  print(main())