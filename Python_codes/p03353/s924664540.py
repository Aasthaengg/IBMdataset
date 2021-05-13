S=input()
s=len(S)
K=int(input())
A=[]
for i in range(s):
  A.append(S[i])
for i in range(s-1):
  A.append(S[i:i+2])
for i in range(s-2):
  A.append(S[i:i+3])
for i in range(s-3):
  A.append(S[i:i+4])
for i in range(s-4):
  A.append(S[i:i+5])
B=sorted(set(A))
print(B[K-1])