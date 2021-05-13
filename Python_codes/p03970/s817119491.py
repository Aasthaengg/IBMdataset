adequate = "CODEFESTIVAL2016"
wrong = input()
cnt = 0

for i in range(len(wrong)):
    if adequate[i] != wrong[i]:
        cnt += 1

print(cnt)