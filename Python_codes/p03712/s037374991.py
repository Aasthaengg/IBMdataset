H, W = list(map(int, input().split()))
con = []

for i in range(H):
  tmp = str(input())
  con.append(tmp)

print("#"*(W+2))
for i in range(H):
  print("#"+con[i]+"#")
print("#"*(W+2))