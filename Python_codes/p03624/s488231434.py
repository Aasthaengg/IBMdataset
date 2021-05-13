import string

S = list(input())

low_list = list(string.ascii_lowercase)
for i in range(len(S)):
    try:
        low_list.remove(S[i])
    except ValueError:
        pass

if len(low_list) == 0:
    print('None')
else:
    print(low_list[0])
