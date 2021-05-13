trump_dictionary = {}
keys = ['S', 'H', 'C', 'D']
for key in keys:
    for num in range(13):
        trump_dictionary[key + ' ' + str(num + 1)] = 0

num = int(raw_input())
counter = 0
while counter < num:
    key = raw_input()
    if key in trump_dictionary:
        trump_dictionary.pop(key)
    counter += 1

for key in keys:
    for num in range(13):
        if key + ' ' + str(num + 1) in trump_dictionary:
            print(key + ' ' + str(num + 1))