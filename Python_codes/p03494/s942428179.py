num = int(input())
vals = list(input().split())

ivals = []
for i in range(num):
  ival = int(vals[i])
  ivals.append(ival)

count = 0
check_flag=0

def is_odd(n):
    """ 奇数判定関数 """
    return (n%2) == 1

while check_flag==0:
  for i in range(num):
    if (ivals[i])%2 != 0:
      check_flag=1
      break
    else:
      ivals[i]=ivals[i]/2
  
  if check_flag==0:
    count+=1

print(count)