suretu = "1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51"
suretu = suretu.split(",")

for i in range(len(suretu)):
    suretu[i] = int(suretu[i])

k = int(input())
if k >= 1 and k <= 32:
    #print(k)
    print(suretu[k-1])