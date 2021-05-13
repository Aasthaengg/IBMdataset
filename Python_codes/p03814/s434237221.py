s=input()
n=len(s)
k=s[::-1]
a=s.index("A")
z=n-k.index("Z")
print(z-a)