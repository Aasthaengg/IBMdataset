a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(input())

S=a,b,c,d,e

if (max(S)-min(S))<=k:
	print("Yay!")
else:
	print(":(")