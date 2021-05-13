import math
while True:
    s=input().split()
    if s[1]=="?":
        break
    elif s[1]=="+":
        print(int(s[0])+int(s[2]))
    elif s[1]=="-":
        print(int(s[0])-int(s[2]))
    elif s[1]=="*":
        print(int(s[0])*int(s[2]))
    elif s[1]=="/":
        print(math.floor(int(s[0])/int(s[2])))
