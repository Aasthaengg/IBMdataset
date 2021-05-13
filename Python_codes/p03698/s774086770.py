s=input()
alp='abcdefghijklmnopqrstuvwxyz'
A=[0 for i in range(26)]
for ss in s:
    A[alp.index(ss)]+=1
print("yes" if all(a<=1 for a in A)==True else "no")