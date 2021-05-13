#ABC047A https://atcoder.jp/contests/abc047/tasks/abc047_a

a,b,c=(int(x) for x in input().split())

max=a
o1=b
o2=c

if b>max:
    max=b
    o1=a

if c>max:
    max=c
    o2=b

if max==(o1+o2):
    print("Yes")
else:
    print("No")

