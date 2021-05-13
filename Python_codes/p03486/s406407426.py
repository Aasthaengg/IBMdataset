s=input()
t=input()
if ("".join(sorted(list(s))))<("".join(sorted(list(t),reverse=True))):
    print("Yes")
else:
    print("No")