N=int(input())
l=list(map(int,input().split()))
ans=[]
for i in range(N):
   for j in reversed(range(N-i)):
      if j+1 == l[j]:
         ans.append(l[j])
         l.pop(j)
         break
      if j == 0:
         print("-1")
         exit()
ans=ans[::-1]
for i in ans:
   print(i)