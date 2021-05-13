num = input()
A = int(num[0])
B = int(num[1])
C = int(num[2])
D = int(num[3])
if 7-A==B+C+D:
  op1='+'
  op2='+'
  op3='+'
elif 7-A==B+C-D:
  op1='+'
  op2='+'
  op3='-'
elif 7-A==B-C+D:
  op1='+'
  op2='-'
  op3='+'
elif 7-A==C+D-B:
  op1='-'
  op2='+'
  op3='+'
elif 7-A==B-C-D:
  op1='+'
  op2='-'
  op3='-'
elif 7-A==C-D-B:
  op1='-'
  op2='+'
  op3='-'
elif 7-A==D-C-B:
  op1='-'
  op2='-'
  op3='+'
elif 7-A==-D-C-B:
  op1='-'
  op2='-'
  op3='-'
print(num[0]+op1+num[1]+op2+num[2]+op3+num[3]+"=7")