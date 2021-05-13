from sys import exit

c = [list(map(int, input().split())) for _ in range(3)]
l_1 = [0, 1, 2]
l_2 = [1, 2, 0]

for i in range(3):
    if not c[l_1[i]][0] - c[l_2[i]][0] == c[l_1[i]][1] - c[l_2[i]][1] == c[l_1[i]][2] - c[l_2[i]][2]:
        print('No')
        exit()
    
    if not c[0][l_1[i]] - c[0][l_2[i]] == c[1][l_1[i]] - c[1][l_2[i]] == c[2][l_1[i]] - c[2][l_2[i]]:
        print('No')
        exit()

print('Yes')