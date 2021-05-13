from bisect import bisect
n=int(input())
lst=sorted(map(int,input().split()))
m=lst[-1]
index=bisect(lst,m/2)
if m!=lst[index]:
    q=lst[index]
    if 0<=index-1:
        p=lst[index-1]
        if abs(m/2-p)>=abs(m/2-q):
            print(m,q)
        else:
            print(m,p)
    else:
        print(m,q)
else:
    print(m,lst[index-1])