N,K = map(int,input().split())

i = 0
anslist = []
while True:
  if N>=K:
    i+=1
    anslist.append(N%K)
    N = N//K
    #print (N)
  if N<K:
    anslist.append(N)
    i+=1
    break
    
anslist.reverse()
#print (anslist)
#print (''.join(map(str, anslist)))
print (i)