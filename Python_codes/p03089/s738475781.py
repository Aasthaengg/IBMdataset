n=int(input())
b=list(map(int,input().split()))
ans=[]
while True:
      for i in range(len(b)-1,-1,-1):
            if b[i]>i+1:
                  print(-1)
                  exit()
            if b[i]==i+1:
                  ans.append(b[i])
                  c=b[i+1:]
                  b=b[:i]
                  b[len(b):len(b)]=c
                  break
      if len(b)==0:
            break
for _ in range(n):
      print(ans.pop())

