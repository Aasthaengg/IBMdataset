N,M=map(int,input().split())
T=1900*M+(N-M)*100
P=1-(1/2)**M
print(int(T/(2**M*(1-P)**2)))