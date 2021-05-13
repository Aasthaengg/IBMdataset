s = list(str(input()))
import itertools
for p in itertools.product(('+', '-'), repeat=3):
    temp = [0]*7
    for i in range(4):
        temp[2*i] = s[i]
    for i in range(3):
        temp[2*i+1] = p[i]
    #print(temp)
    temp = ''.join(temp)
    if eval(temp) == 7:
        print(temp+'=7')
        exit()
