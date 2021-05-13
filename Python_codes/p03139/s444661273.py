N, A, B = map(int, input().split())
s = min(A,B)
t = A+B-N
if t>=0:
    print(s,t)
else:
    print(s, 0)