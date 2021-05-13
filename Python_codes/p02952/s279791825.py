N=int(input())
ans=0

if N<10:
    ans=N
elif N<100:
    ans=9
elif N<1000:
    ans=N-90
elif N<10000:
    ans=909
elif N<100000:
    ans=N-9000-90
else:
    ans=90909
    
print(ans)