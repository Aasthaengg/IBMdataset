H1,M1,H2,M2,K=map(int,input().split())

HM1=H1*60+M1
HM2=H2*60+M2
print(max(HM2-HM1-K,0))