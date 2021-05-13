import sys
 
read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines

def main():

  n=int(input())

  A=[list(map(int,input().split()))[::-1] for i in range(n)]

  day=0
  zan=[n-1]*n
  zann=sum(zan)
  sumi=set(range(n))

  while True:
    day+=1

    kouho=list(sumi)
    sumi=set()
  
    for i in kouho:
      try:
        if A[A[i][-1]-1][-1]-1==i:
          sumi.add(i)
          sumi.add(A[i][-1]-1)
      except:
        pass

    for k in sumi:
      A[k].pop()
      zan[k]-=1

    if zann==sum(zan):
      print(-1)
      exit(0)
  
    zann=sum(zan)
  
    if zann==0:
      print(day)
      exit(0)
    
if __name__ == "__main__":
	main()