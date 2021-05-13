ap,bp = 0,0
n = int(input())
for i in range(n):
    a,b = input().split()
    if a>b:
        ap+=3
    elif a==b:
        ap+=1
        bp+=1
    else:
        bp+=3
print(ap,bp)