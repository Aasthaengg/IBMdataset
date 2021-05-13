a, b, c = input().split()
lst = [a, b, c]
r_lst = sorted(lst, reverse=True)
x = ''.join(n for n in r_lst[:2])
y = ''.join(i for i in r_lst[-1:])
print(int(x)+int(y))
