s=input()
zero = s.count("0")
one = s.count("1")
print(len(s)-abs(zero-one))