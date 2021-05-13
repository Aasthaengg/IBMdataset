S="*"+input()
N=len(S)-1

F=True
for i in range(1,N+1):
    if i%2==1:
        F&=S[i] in {"R","U","D"}
    else:
        F&=S[i] in {"L","U","D"}

if F:
    print("Yes")
else:
    print("No")