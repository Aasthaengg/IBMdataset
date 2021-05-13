from collections import Counter
L=list(map(int,input().split()))
A=Counter(L)
print(A.most_common()[-1][0])