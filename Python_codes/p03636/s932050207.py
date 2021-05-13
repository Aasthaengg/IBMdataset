s = input()
answer = ''
s = list(s)
answer = s[0] + str(len(s)-2) + s[len(s)-1]
print(answer)