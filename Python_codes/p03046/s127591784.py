m,k =map(int,input().split())
if k>=2**m:
  print(-1)
elif [m,k]==[0,0]:
  print("0 0")
elif [m,k]==[1,0]:
  print("0 0 1 1")
elif [m,k]==[1,1]:
  print(-1)
else:
  l=[]
  for iii in range(2**m):
    if iii!=k:
      l.append(iii)
  out=" ".join(map(str,l[::-1]+[k]+l+[k]))
  print(out)