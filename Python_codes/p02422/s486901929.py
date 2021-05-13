s = str(input())
n = int(input())

for i in range(n):
  cmd = list(str(input()).split())
  
  if cmd[0] == 'print':
    print(s[int(cmd[1]):int(cmd[2])+1])
  elif cmd[0] == 'reverse':
    temp = s[int(cmd[1]):int(cmd[2])+1]
    s = s[:int(cmd[1])] + temp[::-1] + s[int(cmd[2])+1:] 
  else: #replace
    s = s[:int(cmd[1])] + cmd[3] + s[int(cmd[2])+1:] 
