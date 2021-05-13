A,B,C = map(int,input().split())
if A%2 == B%2 == C%2 ==1:
    print(A*B*C//max(A,B,C))
else:
    print(0)