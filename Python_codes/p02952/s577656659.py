N=int(input())
ans = 0

if N <= 9:
    ans=N
elif N<=99:
    ans=9
elif N<=999:
     ans=N-100+1+9
elif N<=9999:
    ans=999-100+1+9
elif N<=99999:
    ans=N-10000+1+999-100+1+9
else:
    ans=99999-10000+1+999-100+1+9

print(ans)