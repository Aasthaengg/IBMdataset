num = int(input())
minnum = 10 ** 18 + 1
ans = (-10 ** 9 - 1)
for n in range(num):
    newnum = int(input())
    ans = max(ans,newnum - minnum)
    minnum = min(minnum,newnum)
print(ans)