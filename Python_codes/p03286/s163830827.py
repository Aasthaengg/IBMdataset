
N=int(input())
ans=""
while True:
    if N%2==1:
        ans+="1"
        N-=1
    else:
        ans+="0"
    N=N//(-2)
    if N==0:
        break

print(ans[::-1])
