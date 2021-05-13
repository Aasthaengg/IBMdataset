H1,M1,H2,M2,K=map(int,input().split())

length=(H2*60+M2)-(H1*60+M1)

ans=length-K

print(ans)