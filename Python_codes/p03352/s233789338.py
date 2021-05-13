X = int(input())
tab = set([1])
for i in range(1,X+1):
    for j in range(2,X+1):
        if i**j <= X:
            tab.add(i**j)
        else:
            break
print(max([i for i in tab]))