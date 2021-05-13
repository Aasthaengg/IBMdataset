n=int(input())
s=list(str(input()))
rn=0
bn=0
for i in range(n):
    if s[i]=="R":
        rn+=1
    else:
        bn+=1
print("YNeos"[rn<=bn::2])
