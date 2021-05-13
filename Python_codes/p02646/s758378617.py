A,V=map(int,input().split())
B,W=map(int,input().split())
T=int(input())

if A<B:
    a=V*T
    b=W*T
    a=A+a
    b=B+b
    if b<=a:
        print("YES")
    else:
        print("NO")
elif B<A:
    a=V*T
    b=W*T
    a=A-a
    b=B-b
    if a<=b:
        print("YES")
    else:
        print("NO")
else:
    print("YES")