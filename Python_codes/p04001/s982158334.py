s = input()

def solve(i,psum,tmp):
  if i==len(s):
    return tmp+int(psum)  
  return solve(i+1,s[i],int(psum)+tmp) + solve(i+1,psum+s[i],tmp)

print(solve(1,s[0],0))