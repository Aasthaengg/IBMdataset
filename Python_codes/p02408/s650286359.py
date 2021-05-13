lst = [x+' '+str(y) for x in ['S', 'H', 'C', 'D'] for y in range(1, 14)]
n = int(input())
for i in range(n):
    lst.remove(input())
for x in lst:
    print(x)