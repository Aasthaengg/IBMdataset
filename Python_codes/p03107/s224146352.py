s = input()
red = s.count("0")
blue = s.count("1")

ans = min(red,blue)

print(ans*2)
