s = input()
a = [int(s[i:i+3]) for i in range(len(s)-2)]
a = list(map(lambda x: abs(x-753), a))
print(min(a))