input()
s = input()
while "DI" in s:
    s = s.replace("DI", "")
print(s.count("I"))