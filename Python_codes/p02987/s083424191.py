S = input()
count = 0
same = []
for letter in S:
    if S.count(letter) == 2 and letter not in same:
        same.append(letter)
        count += 1

if count == 2:
    print("Yes")
else:
    print("No")