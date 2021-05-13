A,B,C=map(int,input().split())

a=0
D=set()
while True:
    if A%2!=0 or B%2!=0 or C%2!=0:
        break
    if (A,B,C) in D:
        a=-1
        break
    else:
        D.add((A,B,C))
    p=(B+C)/2
    q=(A+C)/2
    r=(A+B)/2
    A=p;B=q;C=r
    a+=1
print(a)