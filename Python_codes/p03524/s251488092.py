from collections import Counter as co
s=input()
n=len(s)
l=sorted(co(list(s)).values())
if len(l)<=2:
    print("YES") if n==len(l) else print("NO")

else:
    m=l[0]
    for v in l:
        if v-m<=1:continue
        print("NO");exit()

    print("YES")