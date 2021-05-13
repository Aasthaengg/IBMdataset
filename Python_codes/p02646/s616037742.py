A,V= map(int,input().split())
B,W= map(int,input().split())
T = int(input())

d = abs(B-A)
e = V-W

if e*T>=d:
    print("YES")
else:
    print("NO")
