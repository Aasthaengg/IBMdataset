x = int(input())

ans = int(x/11)*2
tmp = x%11
if tmp > 6:
    ans+=2
elif tmp > 0:
    ans+=1
print(ans)
