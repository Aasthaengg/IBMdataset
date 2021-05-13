s = input()
n = len(s)
print(sum(t != u for t, u in zip(s[:n//2], s[-(-n//2):][::-1])))