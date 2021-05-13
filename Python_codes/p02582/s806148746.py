S=input()
N=0
if S[0]=="R":
    N+=1
    if S[1]=="R":
        N+=1
        if S[2]=="R":
            N+=1
elif S[1]=="R":
    N+=1
    if S[2]=="R":
        N+=1
elif S[2]=="R":
    N+=1
print(N)