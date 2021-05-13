op = ['-','+']
line = input().split(' ')
s = 1
if line[1] == op[0]:
  s = -1
print(int(line[0])+(int(line[2])*s))