import sys

n,k = map(int,input().split())
s = input()

zero = []
one = []
string = s[0]
if string == '0':
	flag = True
else:
	flag = False
count = 0
left = 0
right = 0
num = 0
for i in range(n):
	if s[i] == string:
		count += 1
	else:
		if string == '0':
			num = count
			string = '1'
		else:
			one.append(count)
			if num != 0:
				zero.append([num,left,count])
			string = '0'
			left = count
			num = 1
		count = 1

if string == '0':
	zero.append([count,left,0])
else:
	zero.append([num,left,count])
	one.append(count)
#print(zero)
#print(one)
if len(zero) <= k:
	print(len(s))
	sys.exit()
res = 0
for i in range(k):
	res += zero[i][0] + zero[i][1]
res += zero[i][2]
#print(res)
ans = res
for i in range(len(zero)-k):
	res -= zero[i][0] + zero[i][1]
	#print(res)
	res += zero[i+k][0] + zero[i+k][2]
	#print(res)
	ans = max(ans,res)
print(ans)