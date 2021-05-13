S = input().strip()
C = {chr(i):0 for i in range(97,123)}
for i in range(len(S)):
    C[S[i]] += 1
x = "None"
for i in range(97,123):
    if C[chr(i)]==0:
        x = chr(i)
        break
print(x)