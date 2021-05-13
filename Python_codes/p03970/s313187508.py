#Signboard
S = "CODEFESTIVAL2016"
s1 = input()
count = 0
for i in range(16):
    if S[i] != s1[i]:
        count =count + 1
print(count)