N = int(input())
H = list(map(int, input().split()))
Hs = [H]
T, c = 0, 1
while c<100000:
  List_1 = []
  for H in Hs:
    start = 0
    T += min(H)
    H = [h-min(H) for h in H]
    List_2 = [i for i, x in enumerate(H) if x == 0]
    for l in List_2:
      List_1.append(H[start:l])
      start = l+1
    List_1.append(H[start:])
  Hs.clear()
  for List in List_1:
    Hs.append(List)
  Hs = [H for H in Hs if H != []]
  c += 1
print(T)