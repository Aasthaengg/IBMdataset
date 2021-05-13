test_string = input()

words = test_string.split(", ")
cases_switched_strings = []

for word in words:
    cases_switched_strings.append(word.swapcase())

output = ", ".join(cases_switched_strings)

print(output)

