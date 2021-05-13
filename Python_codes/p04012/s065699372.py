import collections
w=list(input())
alpha=[chr(i) for i in range(97, 97+26)]
beautiful=True
C=collections.Counter(w)
for i in alpha:
    if C[i]%2==1:
        beautiful=False
if beautiful:
    print("Yes")
else:
    print("No")