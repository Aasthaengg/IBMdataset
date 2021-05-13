n=int(input())

a=list(map(int,input().split()))

if n==2:
    print(max(a)-min(a))

    print(max(a),min(a))
    exit()

#+ -が最低一つ必要
#あとはどちらの符号にもできる？

a_p=[]
#a_zero=[]
a_m=[]

for aa in a:
    if aa>=0:
        a_p.append(aa)
    else:
        a_m.append(aa)

#どっちもある

ans=[]

if len(a_m)>0 and len(a_p)>0:
    if len(a_p)==1:
        tmp=a_p[0]
        for v in a_m:
            ans.append([tmp,v])
            tmp=tmp-v
    else:
        tmp=a_m[0]
        for v in a_p[1:]:
            ans.append([tmp,v])
            tmp=tmp-v
        ans.append([a_p[0],tmp])
        tmp=a_p[0]-tmp
        for v in a_m[1:]:
            ans.append([tmp,v])
            tmp=tmp-v

elif len(a_p)>0:
    a_p.sort()

    tmp=a_p[0]
    for v in a_p[2:]:
        ans.append([tmp,v])
        tmp=tmp-v
    ans.append([a_p[1],tmp])

else:
    a_m.sort(reverse=True)

    tmp=a_m[0]
    for v in a_m[1:]:
        ans.append([tmp,v])
        tmp=tmp-v


print(ans[-1][0]-ans[-1][1])
for item in ans:
    print(item[0],item[1])



