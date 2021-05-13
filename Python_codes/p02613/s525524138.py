n=int(input())
l=[]
for i in range(n):
    a=input()
    l.append(a)
print('AC x ',l.count('AC'))
print('WA x ',l.count('WA'))
print('TLE x ',l.count('TLE'))
print('RE x ',l.count('RE'))

