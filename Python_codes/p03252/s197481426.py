S = input()
T = input()

chars = "abcdefghijklmnopqrstuvwxyz"
c2n = {chars[i]: i for i in range(26)}
RS = [-1]*26
RT = [-1]*26
N = len(S)
flag = True
for i in range(N):
    if RS[c2n[S[i]]] >= 0:
        if RS[c2n[S[i]]] != c2n[T[i]]:
            flag = False
            break
    if RT[c2n[T[i]]] >= 0:
        if RT[c2n[T[i]]] != c2n[S[i]]:
            flag = False
            break
    if RS[c2n[S[i]]] < 0:
        RS[c2n[S[i]]] = c2n[T[i]]
    if RT[c2n[T[i]]] < 0:
        RT[c2n[T[i]]] = c2n[S[i]]
    
if flag:
    print("Yes")
else:
    print("No")