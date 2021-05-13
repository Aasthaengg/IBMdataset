# coding: utf-8

n = int(raw_input())
for i in range(n):
	data = map(int, raw_input().split())
	if data[0]**2 == data[1]**2 + data[2]**2:
		print("YES")
	elif data[1]**2 == data[2]**2 + data[0]**2:
		print("YES")
	elif data[2]**2 == data[0]**2 + data[1]**2:
		print("YES")
	else:
		print("NO")