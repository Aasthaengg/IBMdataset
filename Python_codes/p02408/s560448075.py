n = int(input())
S = []
H = []
C = []
D = []
for i in range(n):
    mark, num = input().split()
    if mark == "S":
        S.append(int(num))
    elif mark == "H":
        H.append(int(num))
    elif mark == "C":
        C.append(int(num))
    elif mark == "D":
        D.append(int(num))
marks = ['S', 'H', 'C', 'D']
cards = [sorted(S), sorted(H), sorted(C), sorted(D)]
for i in range(4):
    mark = marks[i]
    for num in range(1,14):
        if not(num in cards[i]):
            print('{0} {1}'.format(mark, num))