N=int(input())
s=set()
for i in range(N):
    A=int(input())
    if A in s:
        s.discard(A)
    else:
        s.add(A)
print(len(s))