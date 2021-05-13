s=input()
for i in range(int(input())):
    ope=input().split()
    ope[1]=int(ope[1])
    ope[2]=int(ope[2])
    if ope[0]=="print":
        print(s[ope[1]:ope[2]+1])
    if ope[0]=="replace":
        s=s[:ope[1]]+ope[3]+s[ope[2]+1:]
    if ope[0]=="reverse":
        s=s[:ope[1]]+s[ope[1]:ope[2]+1][::-1]+s[ope[2]+1:]
