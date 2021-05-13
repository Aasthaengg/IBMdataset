S=list(input())
S_odd=S[::2]
S_even=S[1::2]
flag=1
for i in S_odd:
    if i != "R" and i != "U" and i != "D":
        print("No")
        exit(0)
    for j in S_even:
        if j != "L" and j != "U" and j != "D":
            print("No")
            exit(0)
print("Yes")