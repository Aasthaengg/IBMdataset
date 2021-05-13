S = input()
if S != S[::-1]:
    print("No")
    exit()

if S[:len(S)//2] != S[:len(S)//2][::-1]:
    print("No")
    exit()
print("Yes")