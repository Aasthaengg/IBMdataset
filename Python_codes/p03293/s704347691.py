from sys import exit

s = input()
t = input()

def role(str, n):
    return str[n:len(str)] + str[:n]

for i in range(len(s)):
    if role(s,i) == t:
        print('Yes')
        exit()

print('No')