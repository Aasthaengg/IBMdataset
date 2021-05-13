import sys
line = sys.stdin.readline()
n = []
while line:
 num = map(int,line.split())
 if num[0]==0 and num[1] == 0:
 	break;
 else:
 	if num[0] > num[1]:
 		tmp = num[0]
 		num[0] = num[1]
 		num[1] = tmp
 	s = str(num[0])+" "+str(num[1])
 	n.append(s)
 line = sys.stdin.readline()
for i in n:
 print i