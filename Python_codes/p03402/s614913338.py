a,b = map(int,input().split())

p = [["."]*100 for _ in range(20)]
q = [["#"]*100 for _ in range(21)]

for t in range(b-1):
  p[t//50*2][t%50*2] = "#"
for t in range(a-1):
  q[t//50*2+1][t%50*2] = "."
  
print(41, 100)
for l in p+q:
  print("".join(l))
  
