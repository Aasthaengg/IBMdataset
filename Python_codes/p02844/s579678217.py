N=int(input())
S=list(input())
x=list(map(str,list(range(10))))
cnt=0
for i in x:
  if i in S:
    p=S.index(i)
    S1=S[p+1:]
    for j in x:
      if j in S1:
        q=S1.index(j)
        S2=S1[q+1:]
        for k in x:
          if k in S2:
            cnt+=1
print(cnt)