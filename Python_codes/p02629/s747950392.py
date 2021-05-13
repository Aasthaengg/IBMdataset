n=int(input())
ans = []
while n>0:
    if n%26==0:
        ans.append("z")
    else:
        ans.append(chr(96+(n%26)))
    n=(n-1)//26
print(''.join(ans[::-1]))