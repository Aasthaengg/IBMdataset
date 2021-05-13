s = list(input())

num = len(s[1:len(s)-2]) + 1

print(s[0] + str(num) + s[len(s)-1])