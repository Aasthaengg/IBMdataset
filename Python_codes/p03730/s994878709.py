a,b,c=map(int,input().split())

frag='NO'
for i in range(b-1):
  if (i+1)*a%b==c:
    frag='YES'
    break

print(frag)
