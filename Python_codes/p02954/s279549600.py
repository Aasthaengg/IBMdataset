S = input()
A = []
tmp = [0,0]
flag = "R"
for i in range(len(S)):
  if flag == "L" and S[i] == "R":
    A.append(tmp)
    flag = "R"
    tmp = [1,0]
    continue
  elif flag == "R" and S[i] == "L":
    flag = "L"
    
  if S[i] == "R":
    tmp[0]+=1
  elif S[i] == "L":
    tmp[1]+=1
A.append(tmp)
ans = []
for val in A:
  r, l = val
  if (r+l)%2==0:
    ans+=[0]*(r-1)+[(r+l)//2]+[(r+l)//2]+[0]*(l-1)
    continue
  ads = (r+l)//2
  ma = max(r,l)-1
  if r<l:
    if ma%2!=0:
      ans+=[0]*(r-1)+[ads+1]+[ads]+[0]*(l-1)
    else:
      ans+=[0]*(r-1)+[ads]+[ads+1]+[0]*(l-1)
  else:
    if ma%2!=0:
      ans+=[0]*(r-1)+[ads]+[ads+1]+[0]*(l-1)
    else:
      ans+=[0]*(r-1)+[ads+1]+[ads]+[0]*(l-1)
print(" ".join(map(str,ans)))