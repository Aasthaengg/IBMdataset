S=input()
N=len(S)

def rule1():
  return S==S[::-1]

def rule2():
  s = S[:(N-1)//2]
  return s==s[::-1]

def rule3():
  s = S[(N+3)//2-1:]
  return s==s[::-1]  

print ('Yes' if rule1() and rule2() and rule3() else 'No')
