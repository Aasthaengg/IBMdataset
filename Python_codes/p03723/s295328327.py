from sys import stdin

a,b,c = [int(x) for x in stdin.readline().strip().split()]
l = 0
mem = []

while(True):
  if sum([a%2, b%2, c%2]) > 0:
    break
  elif [a,b,c] in mem:
    l = -1
    break
  else:
    l += 1
    mem.append([a,b,c])
    a_tmp = b/2 + c/2
    b_tmp = a/2 + c/2
    c_tmp = a/2 + b/2
    a,b,c = a_tmp,b_tmp,c_tmp
    
print(l)