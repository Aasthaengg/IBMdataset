n=input()
s=""
for i in reversed(n):
    s+=i

if n==s:
    print("Yes")
else:
    print("No")