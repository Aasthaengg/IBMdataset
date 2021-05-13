S = str(input())
M = []
con = 0
for j in S:
  if j == 'A' or j == 'C' or j == 'G' or j == 'T':
    con += 1
  else:
    if con != 0:
      M.append(con)
    con = 0
M.append(con)
print(max(M))