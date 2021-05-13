s = input()
cnt = 0
for i in range(len(s)-1):
    if(s[i] == s[i+1]):
        cnt = cnt + 1
if cnt == 0:
    print("Good")
else:
    print("Bad")