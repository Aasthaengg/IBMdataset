n = int(input())
A=[]
for i in range(n):
    A.append(int(input()))

S = sorted(A,reverse=True)
maxa = S[0]
maxa2 = S[1]
B=[]
B = [maxa2 if a==maxa else maxa for a in A]

for b in B:
    print(b)
