import sys
input = sys.stdin.readline
def main():
  h,w=map(int,input().split())
  a=[list(map(lambda x:0 if x=='#' else -1,list(input()))) for _ in range(h)]
  todo=[]
  from collections import deque
  for i in range(h):
    for j in range(w):
      if a[i][j]==0:
        todo.append([i,j])
  todo=deque(todo)
  ans=0
  while todo:
    i,j=todo.popleft()
    d=a[i][j]+1
    ans=d-1
    if i>0 and a[i-1][j]==-1:
      a[i-1][j]=d
      todo.append([i-1,j])
    if i<h-1 and a[i+1][j]==-1:
      a[i+1][j]=d
      todo.append([i+1,j])
    if j>0 and a[i][j-1]==-1:
      a[i][j-1]=d
      todo.append([i,j-1])
    if j<w-1 and a[i][j+1]==-1:
      a[i][j+1]=d
      todo.append([i,j+1])
  print(ans)
if __name__=='__main__':
  #import datetime
  #print(datetime.datetime.now())
  main()
  #print(datetime.datetime.now())