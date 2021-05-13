a,b,k=map(int,input().split())
l=[]
for i in range(k):
    if a+i<=b:
        if a+i not in l:
            l.append(a+i)#小さい方からk番目以内
    if b-i>=a:
        if b-i not in l:
            l.append(b-i)#小さい方からk番目以内
l.sort()
[print(i) for i in l]