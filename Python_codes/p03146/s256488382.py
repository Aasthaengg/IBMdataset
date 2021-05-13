s = int(input())
List = [s]
c = 2
while c<1000000:
  if s%2==0:
    s = s//2
  else:
    s = 3*s+1
  if s in List:
    print(c)
    break
  else:
    List.append(s)
    c += 1