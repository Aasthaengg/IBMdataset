s = input()

char_number = len(s)

start = s[0]
end   = s[-1]

answer = start + str(char_number - 2) + end
print(answer)