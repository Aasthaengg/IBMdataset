s=input()
f = 0
for i in range(3):
    if(s[i] == s[i+1]):
        f = 1
        break
if f == 1:
    print("Bad")
else:
    print("Good")