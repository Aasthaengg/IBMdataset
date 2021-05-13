n=int(input())
sp=[[] for i in range(n)]
for i in range(n):
  s,p=input().split()
  sp[i] = [i+1, s, int(p)]
sp = sorted(sorted(sp, key=lambda x:x[2], reverse=True), key=lambda x:x[1])
for i in range(n):
  print(sp[i][0])