n = input()

if n[1:] == "9" * (len(n) - 1) :
    num = (int(n[0])) + 9 * (len(n) - 1)
else:
    num = (int(n[0]) - 1) + 9 * (len(n) - 1)

print(num)