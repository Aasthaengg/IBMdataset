s=input()
w=set()
for i in range(len(s)):
    w.add(s[i])
if len(s)==len(w):
    print("yes")
else:
    print("no")