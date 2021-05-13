import fileinput

cnt = 0
W = input()
for line in fileinput.input():
    if line.rstrip() == "END_OF_TEXT":
        break

    cnt += line.lower().split().count(W)

print(cnt)

