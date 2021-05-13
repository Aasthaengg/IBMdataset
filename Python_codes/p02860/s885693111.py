N = int(input())
S=input()

if N%2==0 and all(a==b for a,b in zip(S,S[N//2:])):
    print("Yes")
else:
    print("No")
    
