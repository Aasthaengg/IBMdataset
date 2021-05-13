s = input()

def solve(i,psum,tmp):
  if i==len(s)-1:
    return tmp+int(psum)  
  return solve(i+1,s[i+1],int(psum)+tmp) + solve(i+1,psum+s[i+1],tmp)

print(solve(0,s[0],0))