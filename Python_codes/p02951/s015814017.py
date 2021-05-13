A,B,C = map(int,input().split())

if A-B >= 0:
    print(max(C-(A-B),0))
else:
    print(C)