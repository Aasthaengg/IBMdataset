n=int(input())
w=[0 for i in range(101)]
for m in range(2,n+1):
    tmp=m
    for j in range(2,m+1):
        while tmp%j==0:
            w[j]+=1
            tmp//=j
def num(a):
    return len(list(filter(lambda x:x>=a-1,w)))
print(num(75)+num(25)*(num(3)-1) + num(15) * (num(5) - 1)
+ num(5) * (num(5) - 1) * (num(3) - 2) // 2)