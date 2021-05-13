A,B,C=map(int,input().split())
count=0
while B>0:
   if A>B:
      break
   B=B-A
   count+=1
   if count>=C:
      break
print(count)