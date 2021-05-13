A,B,C = list(map(int,input().strip().split()))

if C - ( A - B ) < 0:
    print(0)
else:
    print(C - (A-B))
