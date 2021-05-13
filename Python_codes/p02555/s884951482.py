def extGCD(a,m):
  if(m==0):
    return a,1,0
  d,s,t = extGCD(m,a%m)
  y=s-(a//m)*t
  x = t
  return d,x,y

def invmod(a,m):
  _,x,_ = extGCD(a,m)
  return x%m
  

S = int(input())
mod_num=int(1.0e+9+7)
max_count = S//3
ans_count=0
for i in range(max_count):
  if(i==0):
    ans_count+=1
    continue
  temp = (i+1)*3
  rest = S-temp+i
  ans_temp=1
  divide_temp = 1
  for j in range(i):
    ans_temp*=rest-j
    ans_temp%=mod_num
    divide_temp*=j+1

  inv_num = invmod(divide_temp,mod_num)

  ans_temp = (ans_temp*inv_num)%mod_num

  ans_count+=ans_temp

print(int(ans_count)%mod_num)
