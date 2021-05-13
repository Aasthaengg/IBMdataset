s = input()
s_length = len(s)
s_first = s[0]
s_last = s[-1]
answer = s_first + str(len(s)-2) + s_last
print(answer)