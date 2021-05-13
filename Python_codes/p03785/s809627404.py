n,c,k=map(int, input().split())
t=[]
for _ in range(n):
  tmp=[int(input())]
  t.extend(tmp)
t.sort()
t.append(10**10)
ans=0
cnt_pssngr=1
fst_pssnger_t=t[0]
for i in range(1,n+1):
  if cnt_pssngr<c and t[i]<=fst_pssnger_t+k:
    cnt_pssngr+=1
  else:
    ans+=1
    cnt_pssngr=1
    fst_pssnger_t=t[i]
print(ans)