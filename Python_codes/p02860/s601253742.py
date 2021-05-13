N=int(input())
S=input()

if N%2:
    print("No")
    exit()

T=S[:N//2]
if S==T+T:
    print("Yes")
else:
    print("No")