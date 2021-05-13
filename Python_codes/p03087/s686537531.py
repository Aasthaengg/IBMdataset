n,q = map(int,input().split())
s = input()

array = [0]*len(s)

for i in range(1,len(s)):
  if( s[i-1:i+1] == "AC" ):
    array[i] = array[i-1] + 1
  else:
    array[i] = array[i-1]
      

for i in range(q):
  l,r = map(int,input().split())
  l -= 1
  r -= 1
  ans = array[r] - array[l]
  print(ans)

 