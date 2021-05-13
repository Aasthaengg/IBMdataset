n = input()
nb=int(n)
a= list(n)
ab = [int(s) for s in a]
z=0
for i in range((len(ab))):
    z+=ab[i]
if nb%9==0 and z%9==0:
    print("Yes")
else:
    print("No")