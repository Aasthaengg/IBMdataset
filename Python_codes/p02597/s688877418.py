N = int(input())
O = input()
ridx = [i for i, s in enumerate(O) if s == 'R']
n = len([i for i in ridx if i >= len(ridx)])
print(n)