n=int(input())
lst=[]
for i in range(n):
  a,b=input().split()
  lst.append([a,b,i+1])
lst.sort(key=lambda x:(x[0],-int(x[1])))
for i in lst:
  print(i[2])