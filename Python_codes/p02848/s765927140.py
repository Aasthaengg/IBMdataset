N = int(input())
S = list(input())
T = []

for i in range(len(S)):
    if ord(S[i])+N <= 90:
        T.append(chr(ord(S[i])+N))
    elif ord(S[i])+N >90:
        T.append(chr(ord(S[i])+N-26))
    
for i in range(len(S)):
    print(T[i], end ='')