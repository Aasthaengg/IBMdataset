n = int(input())
i = []

for x in range(n):
    x = input()
    i.append(x)    

    
print('AC x',i.count('AC'))
print('WA x',i.count('WA'))
print('TLE x',i.count('TLE'))
print('RE x',i.count('RE'))