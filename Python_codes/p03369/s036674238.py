s = input()
counter = 0
if(s[0] == 'o'):
    counter += 1
if(s[1] == 'o'):
    counter += 1
if(s[2] == 'o'):
    counter += 1
cost = 700 + 100*counter
print(cost)
