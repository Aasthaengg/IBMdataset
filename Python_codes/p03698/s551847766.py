s = input()
print(["no", "yes"][len(s) == len(set(s))])