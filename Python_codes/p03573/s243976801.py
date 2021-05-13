import collections
A,B,C=map(int,input().split())
ABC=[A,B,C]
ABC=collections.Counter(ABC)
if ABC[A]==1:
    print(A)
elif ABC[B]==1:
    print(B)
else:
    print(C)