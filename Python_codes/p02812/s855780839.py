input()
S = input()
count = 0
for i in range(0, len(S)):
    if S[i:i+3] == "ABC" : count = count + 1
print(count)