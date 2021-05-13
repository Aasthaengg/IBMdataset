N = int(input())
a = [input().split() for i in range(N)]
Set = {}
n = list(range(1,14))
Set['S'] = n.copy()
Set['H'] = n.copy()
Set['C'] = n.copy()
Set['D'] = n.copy()

for suit,num in a:
    Set[suit].remove(int(num))

for i in Set['S']:
    print("S {}".format(i))
for i in Set['H']:
    print("H {}".format(i))
for i in Set['C']:
    print("C {}".format(i))
for i in Set['D']:
    print("D {}".format(i))