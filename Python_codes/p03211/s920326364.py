S=input()
A=[]
B=[]
for i in range (len(S)-2):
    A.append(int(S[i:i+3]))
for i in range(len(A)):
    B.append(abs(A[i]-753))
print(min(B))