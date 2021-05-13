#!/usr/bin/python3
a,b,c,d = 0,0,0,0
n = int(input())
s=[None]*n
for i in range(n):
	s[i] = input()
for i in range(n):
	if("AC" in s[i]):
		a+=1
	elif("WA" in s[i]):
		b+=1
	elif("TLE" in s[i]):
		c+=1
	elif("RE" in s[i]):
		d+=1
print(f"AC x {a}")
print(f"WA x {b}")
print(f"TLE x {c}")
print(f"RE x {d}")