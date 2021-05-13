S = input()

A = [0]
C = [0]
Q = [0]
a=0
c=0
q=0
for i in range(len(S)):
    if S[i]=="A":
        a+=1
    if S[i]=="C":
        c+=1
    if S[i]=="?":
        q+=1
    A.append(a)
    C.append(c)
    Q.append(q)

a = 1
a0 = 1
a1 = 1
a2 = 1
a3 = 1
for i in range(Q[len(S)]):
    a = (a*3)%(10**9 + 7)
    if i==Q[len(S)]-4:
        a3 = a
    elif i==Q[len(S)]-3:
        a2 = a
    elif i==Q[len(S)]-2:
        a1 = a
    elif i==Q[len(S)]-1:
        a0 = a

count = 0
for i in range(1,len(S)):
    if S[i]=="B":
        count=(count+a0*A[i]*(C[len(S)]-C[i+1])+a1*A[i]*(Q[len(S)]-Q[i+1])+a1*Q[i]*(C[len(S)]-C[i+1])+a2*Q[i]*(Q[len(S)]-Q[i+1]))%(10**9 + 7)
    elif S[i]=="?":
        count=(count+a1*A[i]*(C[len(S)]-C[i+1])+a2*A[i]*(Q[len(S)]-Q[i+1])+a2*Q[i]*(C[len(S)]-C[i+1])+a3*Q[i]*(Q[len(S)]-Q[i+1]))%(10**9 + 7)
print(count)