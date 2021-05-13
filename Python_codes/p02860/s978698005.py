N = int(input())

S = input()
a = len(S)//2
if N%2==1:
    print("No")
    
elif S[:a]==S[a:]:
    print("Yes")

else:
    print("No")