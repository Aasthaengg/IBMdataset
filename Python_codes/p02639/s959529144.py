xlist = list(map(int,input().split()))

ans = [1,2,3,4,5]

for i in range(len(ans)):
  if xlist[i]!=ans[i]:
    print(ans[i])