S=input()
A="abcdefghijklmnopqrstuvwxyz"
minimum=len(S)//2
for a in A:
    ans_max=0
    p=0
    for s in S:
        if a==s:
            ans_max=max(p,ans_max)
            p=0
        else:
            p+=1
    ans_max=max(p,ans_max)
    minimum=min(ans_max,minimum)
print(minimum)