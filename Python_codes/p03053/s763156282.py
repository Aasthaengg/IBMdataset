import sys
input = sys.stdin.readline
def main():
  h,w=map(int,input().split())
  a=[input() for _ in range(h)]
  seen=[[1]*w for _ in range(h)]
  from collections import deque
  todo=deque([])
  for hi,ai in enumerate(a):
    for wj,aij in enumerate(ai):
      if aij=='#':
        seen[hi][wj]=0
        todo.append((hi,wj))
  ans=-1
  while todo:
    ans+=1
    next_todo=[]
    for hi,wi in todo:
      if hi>0 and seen[hi-1][wi]:
        next_todo.append((hi-1,wi))
        seen[hi-1][wi]=0
      if hi<h-1 and seen[hi+1][wi]:
        next_todo.append((hi+1,wi))
        seen[hi+1][wi]=0
      if wi>0 and seen[hi][wi-1]:
        next_todo.append((hi,wi-1))
        seen[hi][wi-1]=0
      if wi<w-1 and seen[hi][wi+1]:
        next_todo.append((hi,wi+1))
        seen[hi][wi+1]=0
    todo=next_todo
  print(ans)
if __name__=='__main__':
  main()