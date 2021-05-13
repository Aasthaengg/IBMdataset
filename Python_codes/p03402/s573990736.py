a,b = map(int,input().split())
l = ['###','#.#','.#.','...']
ans = []
for i in range(a//30+1):
    if i==a//30:
        if a%30==0:
            ans[-2] = l[1]*29+l[0]
            break
        k = max(a%30-1,0)
        ans.append(l[1]*k+l[0]*(30-k))
        ans.append(l[0]*30)
        break
    ans.append(l[1]*30)
    ans.append(l[0]*30)
ans.append(l[3]*30)
for i in range(b//30+1):
    if i==b//30:
        if b%30==0:
            ans[-2] = l[2]*29+l[3]
            break
        k = max(b%30-1,0)
        ans.append(l[2]*k+l[3]*(30-k))
        ans.append(l[3]*30)
        break
    ans.append(l[2]*30)
    ans.append(l[3]*30)
print(len(ans),90)
for i in range(len(ans)):
    print(ans[i])
