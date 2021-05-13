#おとといa、きのうb、今日c
a,b,c = (int(x) for x in input().split())
penki_list = [a,b,c]
print(len(set(penki_list)))
