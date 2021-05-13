N,M = (int(T) for T in input().split())
List = [[] for T in range(0,M)]
for T in range(0,M):
    List[T] = [T]+[int(T) for T in input().split()]

CitySort = sorted(List,key=lambda List:(List[1],List[2]))
Disp = [[] for T in range(0,M)]
Rece = 0
for T in range(0,M):
    if CitySort[T][1]!=Rece:
        Rece = CitySort[T][1]
        Count = 1
        Disp[CitySort[T][0]] = str(Rece).zfill(6)+str(Count).zfill(6)
    else:
        Count += 1
        Disp[CitySort[T][0]] = str(Rece).zfill(6)+str(Count).zfill(6)
        
for T in range(0,M):
    print(Disp[T])