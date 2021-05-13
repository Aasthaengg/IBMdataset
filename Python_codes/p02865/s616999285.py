N = int(input())
ans=0
if N%2==0:
    ans=N/2-1
elif N!=1:
    ans=N/2
print(int(ans))