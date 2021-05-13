number=int(input())
string=input()
characters=len(string)
empty=""
if characters<=number:
    print(string)
else:
   i=0
   while i<=number-1:
       empty+=string[i]
       i=i+1
   print(f"{empty}...")