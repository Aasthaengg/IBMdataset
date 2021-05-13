def judge(bit):
    global l
    for i in range(n):
        if (bit>>i)&1 == 0:
            continue
        for x,y in l[i]:
            if y==1 and (bit>>x)&1==0:
                return False
            if y==0 and (bit>>x)&1==1:
                return False
    return True

n = int(input())
l = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x,y = map(int,input().split())
        l[i].append((x-1,y))
maxi = 0
for bit in range(2**n):
    if judge(bit):
        maxi = max(maxi,str(bin(bit)).count('1'))
print(maxi)