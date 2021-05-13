N = int(input())

from collections import Counter

A = []
for _ in range(N):
    A.append(input())

B = Counter(A)
MaxC = max(B.values())
Arg = list(B.values()).count(MaxC)
C = sorted(B.items(),key=lambda x:(x[1],x[0]))[::-1]
for i in range(Arg):
    print(C[Arg-i-1][0])