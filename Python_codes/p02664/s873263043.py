import re
string = input()
string = re.sub("P\?", "PD", string)
string = re.sub("\?\?\?", "DDD", string)
string = string.replace("?", "D")
print(string)
