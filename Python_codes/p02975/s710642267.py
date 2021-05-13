n=int(input())
s=[int(i) for i in input().split()]
a=1
for l in s:
    a^=l
if a==1:
    print("Yes")
else:
    print("No")