l=list(map(int,input().split()))
n=[n for n in l if l.count(n) == 1]
for i in n:
  print(i)