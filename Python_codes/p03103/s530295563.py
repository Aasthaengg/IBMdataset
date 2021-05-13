n,m = map(int,input().split())
ab = [list(map(int,input().split())) for j in range(n)]
ab.sort(key=lambda x:x[0])
#print(ab)
ans,i = 0,0

while(m>0):
  num = min(ab[i][1],m)
  ans += ab[i][0]*num
  #print(ans,num)
  m -= num
 #print(m)
  i += 1
print(ans)