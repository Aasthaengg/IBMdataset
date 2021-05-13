nb = int(input())
liste=[int(x) for x in input().split()]
liste.sort()
index1 = (nb//2)-1
index2 = (nb//2)
roger =liste[index2]-liste[index1]
print(roger)
