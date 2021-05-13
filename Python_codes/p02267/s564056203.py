n=int(input())
a=input().split()

m=int(input())
b=input().split()

a=[int(i) for i in a]
b=[int(i) for i in b]

a.sort()
b.sort()
cnt=0

for j in range(m):
  if b[j] in a:
    cnt+=1
print(cnt)


