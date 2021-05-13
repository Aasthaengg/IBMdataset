ha, sa, hb, sb = (int(i) for i in input().split())

while True:
    hb -= sa
    if hb <= 0:
        print("Yes")
        break
    ha -= sb
    if ha <= 0:
        print("No")
        break;
