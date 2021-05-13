k,s=map(int,input().split())
ans=0
for x in range(k+1):  #xは 0~kまで  x=0,1,2,.....k
  for y in range(x,k+1): #yはx~k+1まで, 
    z = s-(x+y)  #zはxとyできまる, このときxyzの組み合わせが確定して評価する.
    if z>k or z<y:
      continue
    if x == y and y == z: #x=y=z
      ans+=1
    elif x==y or y == z or z==x:
      ans+=3
    else:
      ans+=6


print(ans)