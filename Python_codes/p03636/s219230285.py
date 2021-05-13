code = input()

#1文字目
first_code = code[0]
last_code = code[len(code)-1]

print(first_code + str(len(code)-2) +last_code)