def divs(num):
    ans = []
    for i in range(1,int(num**(1/2)+1)):
        if num%i == 0:
            ans += [i,num//i]
    return set(ans)
n = int(input())
a = list(map(int,input().split()))
fin = []
ans = [0]*(n+1)
for i in range(n,0,-1):
    # print(i,a[i-1],ans[i])
    if a[i-1]^ans[i]:
        fin += [i]
        div = divs(i)
        # print(div)
        for j in div:
            ans[j] ^= 1
print(len(fin))
print(*fin)