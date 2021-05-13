n,k = map(int,input().split())
s = input()
cnt = 1
arr0 = []
if s[0]=="1":
  arr = [0]
else:
  arr = [0,0]
for i in range(n-1):
  if s[i] == s[i+1]:
    cnt += 1
  else:
    arr0.append(cnt)
    cnt = 1
arr0.append(cnt)
arr += arr0
if s[n-1] == "0":
  arr.append(0)
lsum = [0]*(len(arr)//2)
lsum[0] = arr[0]+arr[1]
for i in range(1,len(arr)//2):
  lsum[i] = lsum[i-1]+arr[2*i]+arr[2*i+1]
arr = [0,0]+[0]*(s[0]=="0")+arr0+[0]*(s[n-1]=="1")
rsum = [0]*(len(arr)//2)
for i in range(1,len(arr)//2):
  rsum[i] = rsum[i-1]+arr[2*i]+arr[2*i+1]
ans = 0
if k >= len(lsum)-1:
  print(n)
  quit()
for i in range(k,len(lsum)):
  ans = max(ans,lsum[i]-rsum[i-k])
print(ans)