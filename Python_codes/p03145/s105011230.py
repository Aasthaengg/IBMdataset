AB,BC,CUm = input().split()
AB = int(AB)
BC = int(BC)
CUm = int(CUm)

if 1 <= AB <= 100:
    if 1 <= BC <= 100:
        if 1 <= CUm <= 100:
            area = (AB * BC )/ 2
            print(int(area))