nb = int(input())
liste = [int(x) for x in input().split()]
compteur = 0
for loop in range(nb-2):
    if (liste[loop+1]>liste[loop] and liste[loop+1]<liste[loop+2]) or (liste[loop+1]<liste[loop] and liste[loop+1]>liste[loop+2]):
        compteur +=1
print(compteur)
