S=int(input())
ans=int(0)
iqs=[1]
for i in range(1,S):
  iqs.append(i*iqs[-1])
#print(iqs)
for i in range(1,S//3+1):
        raw=S-i*3
    #(i-1)とrawの重複組み合わせ
        ans+=iqs[raw+i-1]//iqs[i-1]//iqs[raw]
        ans=ans%(10**9+7)
print(ans)