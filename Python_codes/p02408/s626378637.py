s, h, c, d = [],[],[],[]

n = int(input())

#add cards
for _ in range(n):
    suit, rank = input().split()
    rank = int(rank)
    if suit == "S":
        s.append(rank)
    elif suit == "H":
        h.append(rank)
    elif suit == "C":
        c.append(rank)
    elif suit == "D":
        d.append(rank)

#check cards
s_missing, h_missing, c_missing, d_missing = [],[],[],[]
for i in range(1, 14):
    if i not in s:
        s_missing.append(i) 
    if i not in h:
        h_missing.append(i) 
    if i not in c:
        c_missing.append(i) 
    if i not in d:
        d_missing.append(i) 

#print missing cards
for card in s_missing:
    print("S", card)
for card in h_missing:
    print("H", card)
for card in c_missing:
    print("C", card)
for card in d_missing:
    print("D", card)


