h,w=map(int,input().split())
ans=[["#"]*(w+2)]
for i in range(h):
  temp=list(map(str,input()))
  temp.insert(0,"#")
  temp.append("#")
  ans.append(temp)
ans.append(["#"]*(w+2))
for i in range(h+2):
  print("".join(ans[i]))