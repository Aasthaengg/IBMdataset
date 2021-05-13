import string, sys
sen = sys.stdin.read().lower()

char_dic = {i:0 for i in string.ascii_lowercase}

for j in sen:
    if j in char_dic:
        char_dic[j] += 1

for k in string.ascii_lowercase:
    print("{} : {}".format(k, char_dic[k]))

