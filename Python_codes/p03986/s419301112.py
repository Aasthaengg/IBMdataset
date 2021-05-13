# 05

s = input()
x = 0
y = 0
for i in s:
    if i == 'S':
        y -= 1
    else:
        y += 1
    #print(x, y)
    x = max(x, y)
    
print(x*2)