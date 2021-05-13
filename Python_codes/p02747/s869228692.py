S = list(input())
n = len(S)
c = 0
if n%2 ==1:
    print("No")
else:
    for i in range(n-1):
        if S[i] == "h" and S[i+1] == "i":
            c = c+1
    if c == int(n/2):
        print("Yes")
    else:
        print("No")