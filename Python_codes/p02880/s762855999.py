n=int(input())
l=list()
if n<=5:
  print("Yes")
  exit()
for i in range(2, n//2+1):
    if n % i == 0: 
        if (n//i,i) not in l:
            l.append((i,n//i))
flag=0
for i in l:
    if i[0]<=9 and i[1]<=9:
        flag=1
        print("Yes")
        exit()
if not flag:
    print("No")
