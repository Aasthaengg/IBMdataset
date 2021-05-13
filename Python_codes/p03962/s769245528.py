#ABC046A https://atcoder.jp/contests/abc046/tasks/abc046_a

a,b,c=(int(x) for x in input().split())

if a==b and b==c and c==a:
    print(1)
elif a!=b and b!=c and c!=a:
    print(3)
else:
    print(2)
