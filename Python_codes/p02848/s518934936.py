import string

N=int(input())
S=input()
A=string.ascii_letters.upper()

T=""
for s in S:
    T+=A[(A.index(s)+N)%26]
print(T)
