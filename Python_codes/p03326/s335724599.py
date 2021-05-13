N,M=map(int,input().split())
Appp=[0]*N
Appn=[0]*N
Apnp=[0]*N
Apnn=[0]*N
Anpp=[0]*N
Anpn=[0]*N
Annp=[0]*N
Annn=[0]*N
for i in range(N):
  a,b,c=map(int,input().split())
  Appp[i]=a+b+c
  Appn[i]=a+b-c
  Apnp[i]=a-b+c
  Apnn[i]=a-b-c
  Anpp[i]=-a+b+c
  Anpn[i]=-a+b-c
  Annp[i]=-a-b+c
  Annn[i]=-a-b-c
Appp.sort(reverse=True)
Appn.sort(reverse=True)
Apnp.sort(reverse=True)
Apnn.sort(reverse=True)
Anpp.sort(reverse=True)
Anpn.sort(reverse=True)
Annp.sort(reverse=True)
Annn.sort(reverse=True)
print(max(sum(Appp[:M]),sum(Appn[:M]),sum(Apnp[:M]),sum(Apnn[:M]),sum(Anpp[:M]),sum(Anpn[:M]),sum(Annp[:M]),sum(Annn[:M])))




