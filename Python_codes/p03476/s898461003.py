def is_prime(n):
    max_factor = int(n**.5)
    for i in range(2, max_factor+1):
        if n % i == 0:
            return False
    return True
  
def is_2017like(n):
    if n % 2 == 0: return False
    return is_prime(n) and is_prime((n+1)//2)
  
cum = [0,0]
for i in range(2,10**5+2):
    if is_2017like(i):cum.append(cum[-1]+1)
    else:cum.append(cum[-1])

Q=int(input())
for q in range(Q):
  l,r=map(int,input().split())
  print(cum[r]-cum[l-1])