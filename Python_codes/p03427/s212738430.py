n = list(input())
n = list(map(int,n))
m = len(n)
if m == 1:
    print(n[0])
elif len(set(n)) == 1 and n[0] == 9:
    print(9 * m)
elif len(set(n)) == 2 and n[0] != 9 and n[1] == 9:
    print(n[0] + (m - 1) * 9)
else:
    print(n[0] - 1 + (m - 1) * 9)