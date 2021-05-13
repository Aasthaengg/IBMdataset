n,m=map(int,input().split())

ans=0
success_probability=1
failure_probability=1
for i in range(1,1000):
    time=(1900*m + 100*(n-m))*i
    success_probability=failure_probability * (1/2**m)
    failure_probability=failure_probability * (1-(1/2**m))
    ans+= time * success_probability

print(round(ans))
