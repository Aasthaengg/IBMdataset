def notExistOdd(lst):
    for i in lst:
        if i%2==1:
            return False
    return True

n=int(input())
a=[int(i)for i in input().split()]
res=0
div=lambda x:x/2
while notExistOdd(a):
    res+=1
    a=list(map(div,a))
print(res)