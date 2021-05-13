S = input()
a = "CODEFESTIVAL2016"
cnt = 0

for i in range(len(a)):
    if S[i] != a[i]:
        cnt += 1

print (cnt)
