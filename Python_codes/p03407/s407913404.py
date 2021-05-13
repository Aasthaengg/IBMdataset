s = input().split()
s = [int(i) for i in s]
print("Yes") if s[0] + s[1] >= s[2] else print("No")