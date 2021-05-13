g1 = [1, 3, 5, 7, 8, 10, 12]
g2 = [4, 6, 9, 11]
g3 = [2]
result = 'No'
x, y = map(int, input().split())

if x in g1:
    if y in g1:
        result = 'Yes'
elif x in g2:
    if y in g2:
        result ='Yes'
print(result)