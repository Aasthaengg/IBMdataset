A=input()
cnt=0
tmp=A[0]
for i in A:
   if tmp!=i:
      cnt+=1
      tmp=i
print(cnt)