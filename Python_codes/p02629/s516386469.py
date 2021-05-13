N=int(input())
ans=""
while N>0:
    tmp=(N-1)%26
    ans=chr(int(tmp)+97)+ans
    N=int((N-tmp)/26)
print(ans)