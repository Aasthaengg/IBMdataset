N = int(input())
s = str(N)
t=""
for i in range(3):
    t = s[i]+t

if t==s:
    print("Yes")
else:
    print("No")