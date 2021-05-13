m, k = map(int,input().split())
if m == 0:
  if k == 0:
    print("0 0")
  else:
    print(-1)
  quit()
  
if m == 1:
    if k == 0:
        print("0 0 1 1")
    else:
        print(-1)
    quit()

n = 2**m
if k >= n:
    print(-1)
    quit()
    
a = list(range(0,k)) + [k] + list(range(0,k))[::-1] + list(range(k+1,n))[::-1]  + [k] + list(range(k+1,n))
b = [str(t) for t in a]
print(" ".join(b))
    
  
  
