count = 0
word = "".join([x.lower() for x in input().split()])
while True:
    line = input().split()
    if "END_OF_TEXT" in line:
        break
    for s in line:
        if word == "".join([x.lower() for x in s]):
            count += 1
print(count)