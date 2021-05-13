import numpy as np
S=input()

num=np.zeros(26)
for i in range(len(S)):
    num[int(ord(S[i]))-97]+=1

zero=[i for i, num in enumerate(num) if num==0]
if zero==[]:
    print("None")
else:
    print(chr(zero[0]+97))