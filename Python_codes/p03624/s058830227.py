S = input().strip()
C = {chr(i):0 for i in range(97,123)}
for i in range(len(S)):
    C[S[i]] += 1
flag = 0
a = 0
for i in range(97,123):
    if C[chr(i)]==0:
        a = chr(i)
        flag = 1
        break
if flag==1:
    print(a)
else:
    print("None")