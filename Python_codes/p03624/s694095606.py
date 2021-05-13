S = input()
exist = [False] * 26
char = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(S)):
    for j in range(26):
        if S[i] == char[j]:
            exist[j] = True
            break
for i in range(26):
    if exist[i] == False:
        print(char[i])
        exit()
print("None")
