s = input()
c = int((len(s) - 1)/2)
ans = (list(s) == list(reversed(s)) and list(s[:c]) == list(reversed(s[:c])) and list(s[(c+1):]) == list(reversed(s[(c+1):])))
print(["No", "Yes"][ans])