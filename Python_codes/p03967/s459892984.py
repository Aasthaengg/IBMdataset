S = input()
g = 0
p = 0
ans = 0
for s in S:
    if s=="g":
        if g>p:
            p+=1
            ans+=1
        else:
            g+=1
    else:
        if g>p:
            p+=1
        else:
            g+=1
            ans-=1
print(ans)