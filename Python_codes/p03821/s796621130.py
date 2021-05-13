n = int(input())
a_input = [0]*n
b_input = [0]*n
for i in range(n):
    a_input[i],b_input[i]=map(int,input().split())

a_input=a_input[::-1]
b_input=b_input[::-1]

ans=0
for i in range(n):
    a = a_input[i]+ans
    b = b_input[i]
    tmp = a%b
    if tmp==0:
        continue
    ans+=(a//b+1)*b-a
print(ans)
