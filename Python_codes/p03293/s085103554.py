s = list(input())
t = list(input())
for i in range(len(s)) :
    s = s[1:] + s[:1]
    if s == t :
        print("Yes")
        break
else :
    print("No")
