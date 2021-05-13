s = list(input())
red = s.count("0")
blue = len(s) - red

print(min(red, blue)*2)