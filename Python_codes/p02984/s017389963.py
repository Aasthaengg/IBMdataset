n = int(input())

a = list(map(int,input().split()))

allw = sum(a)

for i in range(1,len(a),2):
    allw -= 2*a[i]

x = allw

for i in range(n):
    print(x,end = " ")
    x = a[i]*2-x