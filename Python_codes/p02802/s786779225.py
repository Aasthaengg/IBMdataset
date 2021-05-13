n,m=map(int,input().split())
ans = [0]*n
tmp = [0]*n
pen = [0]*n
for i in range(m):
  inp = input().split()
  if inp[1] == "AC":
    ans[int(inp[0])-1] = 1
    pen[int(inp[0])-1] = tmp[int(inp[0])-1]
  elif inp[1] == "WA":
    if ans[int(inp[0])-1] == 0:
      tmp[int(inp[0])-1] += 1
        
print("{0} {1}".format(sum(ans),sum(pen)))