n=int(input())
s=input()
t=s.split("R")
k="".join(t)
nb=len(k)
nr=n-nb
if nr>nb:
    print("Yes")
else:
    print("No")