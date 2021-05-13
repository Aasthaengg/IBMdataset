S = input()
words = ["dream", "dreamer", "erase", "eraser"]
while len(S) > 0:
    flag = True
    for word in words:
        if S.endswith(word):
            flag = False
            S = S[:-len(word)]
    if flag:
        print("NO")
        exit(0)
print("YES")