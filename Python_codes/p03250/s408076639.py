str = input().split(" ")
str.sort(reverse=True)

print(int(str[0] + str[1]) + int(str[2]))
