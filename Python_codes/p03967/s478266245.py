s = input()
print(len(list(filter(lambda x: x == 'g',
                      s[1::2]))) - len(list(filter(lambda x: x == 'p', s[0::2]))))
