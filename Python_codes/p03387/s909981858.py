L=list(map(int,input().split()))
L.sort(reverse=True)

key=(L[0]-L[1])
Key=(L[0]-L[2])
if (key+Key)%2==0:
  print((key+Key)//2)
else:
  print((key+Key)//2+2)