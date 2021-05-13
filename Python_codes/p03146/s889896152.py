s = int(input())
ans = 1
while s!=4 and s!=2 and s!=1:
    if s%2==0: s//=2
    else: s=s*3+1
    ans+=1
print(ans+3)