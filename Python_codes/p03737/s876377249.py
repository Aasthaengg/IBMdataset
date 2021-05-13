s_list = list(input().split())

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

string = ''
for s in s_list:
    idx = ascii_lowercase.find(s[0])
    string += ascii_uppercase[idx]

print(string)