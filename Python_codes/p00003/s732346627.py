n=int(input())
for i in range(n):
    c,d,b=map(int,input().split())

    if c*c+d*d==b*b or c*c+b*b==d*d or b*b+d*d==c*c:
        print("YES")
    else:
        print("NO")
