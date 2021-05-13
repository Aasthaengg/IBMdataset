n=int(input())
l=sorted(list(map(int,input().split())))

num=int(n/2)
if l[num]==l[num-1]:
  print(0)
else:
  print(l[num]-l[num-1])