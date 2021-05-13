def LI():
    return list(map(int, input().split()))


N = LI()
N.sort()
A, B, C = N
a = (C-A)//2
A += a*2
b = (C-B)//2
B += b*2
if A == B == C:
    ans = a+b
elif A == B:
    ans = a+b+1
else:
    ans = a+b+2
print(ans)
