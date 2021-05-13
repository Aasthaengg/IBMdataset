n = int(input())
c = {
    'S': [0]*13,
    'H': [0]*13,
    'C': [0]*13,
    'D': [0]*13
}
for i in range(n):
    chara, number = input().split()
    c[chara][int(number) - 1] = 1

for i in ["S", "H", "C", "D"]:
    for j in range(13):
        if c[i][j] == 0:
            print("{0} {1}".format(i, j+1))

