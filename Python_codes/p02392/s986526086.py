import re

given = input("")

result = re.search(r"([0-9]+)\s([0-9]+)\s([0-9]+)", given)

a = int(result.group(1))
b = int(result.group(2))
c = int(result.group(3))

if a < b and b < c:
    print("Yes")

else:
    print("No")