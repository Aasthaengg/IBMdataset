n = int(input())
ans = ""
if n == 0:
    print(0)
    exit()
while n != 0:
    tmp = n % 2
    ans+=str(tmp)
    n=(n-tmp)//(-2)
ans = ans[::-1]
print(ans)