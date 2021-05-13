N=int(input())
ans=100000000000
for a in range(1,N):
    b=N-a
    tempa=0
    tempb=0
    for i in range(len(str(a))):
        tempa+=a%10
        a=a//10
    for j in range(len(str(b))):
        tempb+=b%10
        b=b//10
    if tempa+tempb<ans:
        ans=tempa+tempb

print(ans)
