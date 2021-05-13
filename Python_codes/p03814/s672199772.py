s = input()

left = s.find("A")
right = s.rfind("Z")

print(right - left + 1)