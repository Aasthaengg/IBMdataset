str0=input()
q=int(input())
for i in range(q):
  ord=input()
  if "print" in ord:
    buff=ord.split()
    a=int(buff[1])
    b=int(buff[2])
    print(str0[a:b+1])
  if "replace" in ord:
    buff=ord.split()
    a=int(buff[1])
    b=int(buff[2])
    str0=str0[0:a]+buff[3]+str0[b+1:]
  if "reverse" in ord:
    buff=ord.split()
    a=int(buff[1])
    b=int(buff[2])
    tmp=str0[a:b+1]
    str0=str0[0:a]+''.join(list(reversed(tmp)))+str0[b+1:]

