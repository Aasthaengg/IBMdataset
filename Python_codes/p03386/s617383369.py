def main():
  a,b,k = list(map(int,input().split()))
  minlist=[]
  maxlist=[]
  ans=[]
  for i in range(0,k):
    if b-i>=a:
      minlist.append(a+i)
    if b-i>=a+k:
      maxlist.insert(0,b-i)
  ans=minlist+maxlist
  set(ans)
  for i in range(0,len(ans)):
    print(ans[i])
main()
