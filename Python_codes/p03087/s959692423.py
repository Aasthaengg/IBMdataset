n,q = map(int,input().split())
s = input()
u = [ list(map(int,input().split())) for _ in range(q)]

c = [0]
count = 0
for i in range(1,n):
  #print(s[i-1] + s[i])
  if s[i-1] + s[i] == 'AC':
    count += 1
  c.append(count)

for i,j in u:
  print( c[j-1] - c[i-1] )
