n = int(input())
s = []
for i in range(n):
  a , b  = input().split()
  s.append((a,int(b),i+1))

s1 = sorted(s,key = lambda S:S[1],reverse=True)
s2 = sorted(s1,key = lambda S:S[0])
for i in range(n):
  print(s2[i][2])