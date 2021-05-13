n=int(input())
lst=[int(input()) for i in range(n)]
ans=sum(lst)
if ans%10!=0:
    print(ans)
    exit()

lst.sort()
for i in lst:
    if i%10!=0:
        lst.remove(i)
        print(sum(lst))
        exit()

print(0)