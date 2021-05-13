k, x = map(int, input().split())
d = {1:'Yes', 0:'No'}
print(d[k*500 >= x])