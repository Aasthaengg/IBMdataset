n=int(input())
l=[int(x) for x in input().split()]

l.sort()
ans=0

for i in range(len(l)-2):
    for j in range(i+2,len(l)):
        a=l[i]
        c=l[j]
        b_min=i+1
        b_max=j-1
        while b_max-b_min>1:
            if l[(b_max+b_min)//2]>c-a:
                b_max=(b_max+b_min)//2
            else:
                b_min=(b_max+b_min)//2
        if l[b_min]>c-a:ans+=j-b_min
        elif l[b_max]>c-a:ans+=j-b_max
print(ans)