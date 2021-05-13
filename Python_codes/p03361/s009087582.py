h,w = map(int,input().rsplit())
s = []
s.append("."*(w+2))
for i in range(h):
	s.append("."+input()+".")
s.append("."*(w+2))
count = 0
ans = 0
for i in range(1,h+1):
	for j in range(1,w+1):
		if s[i][j] == "#":
			if s[i-1][j] == "#":
				count+=1
			elif s[i+1][j] == "#":
				count +=1
			elif s[i][j-1] == "#":
				count +=1
			elif s[i][j+1] == "#":
				count +=1
			else:
				ans = 1
				break

if ans == 0:
	print("Yes")
if ans == 1:
	print("No")