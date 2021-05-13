N=int(input())
S=input()
str="ABC"
c=0
i=2
while i<=N-1:
    if S[i] == "C":
        if S[i-1]=="B":
            if S[i-2]=="A":
                c+=1
                i+=3
            else:
                i+=3
        else:
            i+=3
    else:
        i+=1
print(c)