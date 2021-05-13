s = input()

r = ["RRS","RRR","RSR","SRR","SSR","RSS","SSS","SRS"]
ra = [2,3,1,2,1,1,0,1]
for i in range(8):
    if r[i] == s:
        print(ra[i])