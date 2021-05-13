A,B=map(int,input().split())

G=list()
for i in range(50):
  G.append(['#']*100)
for i in range(50):
  G.append(['.']*100)

for i in range(A-1):
  G[2*(i//50)][2*(i%50)]='.'
for i in range(B-1):
  G[50+2*(i//50)+1][2*(i%50)]='#'

print(100,100)
for i in range(100):
  print(''.join(G[i]))
