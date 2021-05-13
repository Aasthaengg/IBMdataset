n,a,b=map(int,input().split())

def digisum(m):
  if m<10:
    return m
  else:
    return digisum(m//10)+m%10

print(sum(x for x in range(1,n+1) if a<=digisum(x)<=b))
