n=int(input())
s=input()

ecount=s.count("E")
wcount=0
mn=n
for i in range(n):
    if s[i]=="E":
        ecount-=1
        count=ecount+wcount
        if mn>count:
            mn=count
    else:
        count=ecount+wcount
        if mn>count:
            mn=count
        wcount+=1

print(mn)
