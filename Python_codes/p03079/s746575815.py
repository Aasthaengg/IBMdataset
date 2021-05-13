nagasa_str = input().split(" ")
A_len = int(nagasa_str[0])
B_len = int(nagasa_str[1])
C_len = int(nagasa_str[2])

if (A_len==B_len and B_len==C_len):
	print("Yes")
else:
	print("No")