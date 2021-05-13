s = input()

answer_list = []

for i, char in enumerate(s, 1):
    if i % 2 == 1:
        answer_list.append(char)

print("".join(answer_list))