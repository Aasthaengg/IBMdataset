ring = raw_input() * 2
word = raw_input()

flag = 0
counter = 0
while counter < len(ring)/2:
    if ring[counter:(counter + len(word))] == word:
        flag = 1
        break
    counter += 1

if flag:
    print("Yes")
else:
    print("No")