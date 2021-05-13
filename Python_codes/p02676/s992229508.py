k = int(input()) 

s = input() 
string = ''

if k < len(s):
    for x in range(k):
        #''.join(s[x])
        string = string + s[x]
    string = string + '...'
else:
    string = s

print(string)