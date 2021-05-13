N=int(input())
S=input()
S=list(map(int,S))
ans=0
for s in range(1000):
      A=s//100
      B=(s-A*100)//10
      C=s-A*100-B*10
      isOne=0
      isTen=0
      isHundred=0
      for i in range(N) :
        if isOne==0:
          if S[i]==A: 
            isOne=1
        elif isTen==0:
          if S[i]==B: 
            isTen=1
        elif isHundred==0:
          if S[i]==C:
            isHundred=1
            ans+=1
        else:
          break

print(ans)