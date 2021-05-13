Odd = ["R","U","D"]
Even = ["L","U","D"]
match = 0

S = input()

for i in range(len(S)):
    if (i+1) % 2 == 0 and S[i] in Even:
        match += 1
    elif (i+1) % 2 == 1 and S[i] in Odd:
        match += 1

if match == len(S):
    print("Yes")
else:
    print("No")