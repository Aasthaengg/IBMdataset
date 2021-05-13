n = int(input())
L = input()

S = set()
cnt = 0
for i in range(1000):
    i = str(i).zfill(3)
    num = 0
    for j in range(n):
        if L[j] == i[0] and num == 0:
            num =1
        elif L[j] == i[1] and num == 1:
            num =2
        elif L[j] == i[2] and num == 2:
            S.add(i)
            
print(len(S))