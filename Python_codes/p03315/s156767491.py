S = input()
num = 0
for i in range(len(S)):
    if S[i] == '+': num = num + 1
    else : num = num -1
print(num)