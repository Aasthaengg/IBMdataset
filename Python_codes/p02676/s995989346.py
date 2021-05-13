N=int(input())
a=input()
i=0
he=""
if len(a)>N:
    for m in range(N):
        he=he+a[i]
        i=i+1
    he=he+"..."
    print(he)
else:
  print(a)
