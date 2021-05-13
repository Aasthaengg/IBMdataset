s={i:list(input()) for i in 'abc'}
d = 'a'
while s[d]:
    d = s[d].pop(0)
print(d.upper())