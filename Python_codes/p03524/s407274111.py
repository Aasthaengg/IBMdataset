s = input()
a = [0]*3
for i in s:
    a[ord(i)-97] += 1
a = sorted(a)
A=a[2]
B=a[0]
if A-B>=2:
    print("NO")
else:
    print("YES")