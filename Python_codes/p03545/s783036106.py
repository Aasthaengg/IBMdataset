N=list(input())
A=int(N[0])
B=int(N[1])
C=int(N[2])
D=int(N[3])
if A+B+C+D==7:
  key=N[0]+'+'+N[1]+'+'+N[2]+'+'+N[3]+'=7'
  print(key)
  exit()
if A+B+C-D==7:
  key=N[0]+'+'+N[1]+'+'+N[2]+'-'+N[3]+'=7'
  print(key)
  exit()
if A+B-C+D==7:
  key=N[0]+'+'+N[1]+'-'+N[2]+'+'+N[3]+'=7'
  print(key)
  exit()
if A-B+C+D==7:
  key=N[0]+'-'+N[1]+'+'+N[2]+'+'+N[3]+'=7'
  print(key)
  exit()
if A-B-C+D==7:
  key=N[0]+'-'+N[1]+'-'+N[2]+'+'+N[3]+'=7'
  print(key)
  exit()
if A-B+C-D==7:
  key=N[0]+'-'+N[1]+'+'+N[2]+'-'+N[3]+'=7'
  print(key)
  exit()
if A+B-C-D==7:
  key=N[0]+'+'+N[1]+'-'+N[2]+'-'+N[3]+'=7'
  print(key)
  exit()
if A-B-C-D==7:
  key=N[0]+'-'+N[1]+'-'+N[2]+'-'+N[3]+'=7'
  print(key)
  exit()