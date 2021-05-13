string = input()
string_length = len(string)
print(string[0] + "%d" % (string_length - 2) + string[string_length - 1])