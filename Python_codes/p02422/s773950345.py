s=input()
q=int(input())

for i in range(q):
  command=list(input().split(' '))

  if command[0]=='reverse':
    a=int(command[1])
    b=int(command[2])
    s_list=list(reversed(s[a:b+1]))
    s=s[:a]+''.join(s_list)+s[b+1:]

  if command[0]=='replace':
    a=int(command[1])
    b=int(command[2])
    p=command[3]
    s=s[:a]+p+s[b+1:]

  if command[0]=='print':
    a=int(command[1])
    b=int(command[2])
    print(s[a:b+1])
