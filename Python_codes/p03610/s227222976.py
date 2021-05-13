s = input()

lis = [s[i] for i in range(len(s)) if i%2 == 0]
print("".join(lis))