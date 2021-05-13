result = []
while True:
    info = [int(n) for n in input().split()]
    if info[0]==info[1]==info[2]==-1:
        break
    elif -1 in info[:2]:
        result.append("F")
    elif info[0] + info[1] >= 80:
        result.append("A")
    elif 65 <= info[0] + info[1] < 80:
        result.append("B")
    elif 50 <= info[0] + info[1] < 65:
        result.append("C")
    elif 30 <= info[0] + info[1] < 50 and info[2] >= 50:
        result.append("C")
    elif 30 <= info[0] + info[1] < 50:
        result.append("D")
    else:
        result.append("F")
for i in result:
    print(i)
    
