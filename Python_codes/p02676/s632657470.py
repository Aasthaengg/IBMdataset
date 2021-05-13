k=int(input())
s=input()
characters=len(s)
empty=""
if characters<=k:
    print(s)
else:
   i=0
   while i<=k-1:
       empty+=s[i]
       i=i+1
   print(f"{empty}...")