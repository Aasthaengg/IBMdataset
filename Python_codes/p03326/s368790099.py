########10進法からn進法への変換関数部分##############
def format(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
############################

######## 10進法からn進法への変換関数(m桁埋める)部分 ##############
def format0(X, n, m):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    if len(out) < m:
        out = "0" * (m - len(out)) + out
    return out
############################
n,m=map(int,input().split())
if m == 0:
  print(0)
  exit()
xyz = [list(map(int,input().split())) for i in range(n)]
a=[]
for i in range(8):
  i = format0(i,2,3)
  if i == "000":
    li = [-i[0]-i[1]-i[2] for i in xyz]
  elif i == "001":
    li = [-i[0]-i[1]+i[2] for i in xyz]
  elif i == "010":
    li = [-i[0]+i[1]-i[2] for i in xyz]
  elif i == "011":
    li = [-i[0]+i[1]+i[2] for i in xyz]
  elif i == "100":
    li = [i[0]-i[1]-i[2] for i in xyz]
  elif i == "101":
    li = [i[0]-i[1]+i[2] for i in xyz]
  elif i == "110":
    li = [i[0]+i[1]-i[2] for i in xyz]
  else:
    li = [i[0]+i[1]+i[2] for i in xyz]
  li.sort()
  li = li[-m:]
  a.append(sum(li))
print(max(a))
