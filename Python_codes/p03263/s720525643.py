import sys
input = sys.stdin.readline
def main():
  h,w=map(int,input().split())
  a=[list(map(lambda x:int(x)%2,input().split())) for _ in range(h)]
  ans=[]
  for i in range(h):
    for j in range(w):
      if j<w-1 and a[i][j]==1:
        a[i][j]-=1
        a[i][j+1]+=1
        a[i][j+1]%=2
        ans.append([i,j,i,j+1])
      elif i<h-1 and a[i][j]==1:
        a[i][j]-=1
        a[i+1][j]+=1
        a[i+1][j]%=2
        ans.append([i,j,i+1,j])
  print(len(ans))
  for x1,y1,x2,y2 in ans:
    print(x1+1,y1+1,x2+1,y2+1)
if __name__=='__main__':
  main()
