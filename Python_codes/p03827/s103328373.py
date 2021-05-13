n = int(input())
s = input()
count = 0
count_list = [0]

for i in range(len(s)):
    if s[i] == "I":
        count += 1
        count_list.append(count)
    else:
        count -= 1
        count_list.append(count)

print(max(count_list))
