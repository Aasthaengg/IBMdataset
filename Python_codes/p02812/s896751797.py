n = int(input())
s = input()

s = s.replace("ABC", "")

# print(s)

print(int((n - len(s))/3))
