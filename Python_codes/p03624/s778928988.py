alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s1 = str(input())
s = []
for i in s1:
    s.append(i)
s = list(set(s))
s.sort()
x = 'None'
for h in alp:
    if h not in s:
        x = h
        break
print(x)
