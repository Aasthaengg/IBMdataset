N,K = list(map(int,(input()).split()))
kubaru =[]
for n,k in enumerate(range(K)):
#  print(n,k)
  if n+1 != K:
    kubaru.append(1)
    N-=1
  else:
    kubaru.append(N)

print(max(kubaru)-min(kubaru))    
