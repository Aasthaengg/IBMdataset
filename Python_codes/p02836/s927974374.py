s = input()
print(sum(t != u for t, u in zip(s[:len(s)//2], s[::-1])))