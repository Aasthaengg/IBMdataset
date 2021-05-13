N=int(input())
ans=''
for i in range(33):
    if N%pow(2,i+1):
        ans+='1'
        N-=pow(-2,i)
    else:
        ans+='0'
print(int(ans[::-1]))