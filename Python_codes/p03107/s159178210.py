S = input()

length = len(S)
total = 0
for i in list(S):
    total += int(i)

if (length - total) > total:
    answer = total * 2
else:
    answer = (length - total) * 2

print(answer)