n = int(input())
s = input()
red = s.count("R")
blue = n-red
print("Yes" if red > blue else "No")