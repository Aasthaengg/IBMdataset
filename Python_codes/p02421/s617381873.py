n = int(input())
ta = 0
ha = 0

for i in range(n):
    taha = list(map(str, input().split()))
    jud = sorted(taha)
    #print(taha)
    #print(jud)
    if taha[0] == taha[1]:
        ta += 1
        ha += 1
    
    elif taha[0] == jud[0]:
        ha += 3

    else:
        ta += 3

print("{} {}" .format(ta, ha))
