S = input()

cnt = 0
for i in range(len(S)):
    if i % 2 == 0 and S[i] == "R" or S[i] == "U" or S[i] == "D":
        cnt += 1
    elif i % 2 == 1 and S[i] == "L" or S[i] == "U" or S[i] == "D":
        cnt += 1

if cnt == len(S):
    print("Yes")
else:
    print("No")