s = input()
n = len(s)
p = list(s[2:(n-1)])
if s[0] == "A":
    flag = 1
else:
    print("WA")
    quit()
cnt = 0
for i in range(2,n-1):
    if s[i] == "C":
        cnt += 1
    elif s[i].isupper():
        flag = 0
if flag and s[1].islower() and s[n-1].islower() and cnt==1:
    print("AC")
else:
    print("WA")