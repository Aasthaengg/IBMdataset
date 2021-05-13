S = list(input())
Slist = list()

def split_list(S):
  Slist.append(int(''.join(S)))
  N = len(S)
  if N == 1:
    return
  for n in range(1, N):
    S1 = ''.join(S[:n])
    r = 2**(N-n-1)
    
    for i in range(r):
    	Slist.append(int(S1))
    
    split_list(S[n:])
    
  

split_list(S)
ans = sum(Slist)
print(ans)