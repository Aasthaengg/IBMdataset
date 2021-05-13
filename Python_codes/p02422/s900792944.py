st=input()
n=int(input())
for i in range(n):
  moji=list(map(str,input().split()))

  a=int(moji[1])
  b=int(moji[2])
  if moji[0]=="print":
    print(st[a:b+1])
  if moji[0]=="reverse":
    st=st[:a] + st[a:b+1][::-1] + st[b+1:]
  if moji[0]=="replace":
    st=st[:a]+moji[3]+st[b+1:]
