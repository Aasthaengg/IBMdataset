s = sorted(input())
t = sorted(input(), reverse=True)
print(["No", "Yes"][s < t])