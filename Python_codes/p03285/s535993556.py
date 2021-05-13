n = int(input())
a = 'No'
for i in range(100):
    for j in range(100):
        if n == 4*i + 7*j :
            a = 'Yes'

print(a)
