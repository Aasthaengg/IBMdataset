n=int(input())
n1=list(str(n))
n2=n1.copy()
n2.reverse()
n3=int("".join(n2))
if n==n3:
    print("Yes")
else:
    print("No")

