# coding: utf-8
l = list(map(int,input().split()))
if sorted(l)==sorted([1,4,7,9]):
    print("YES")
else:
    print("NO")