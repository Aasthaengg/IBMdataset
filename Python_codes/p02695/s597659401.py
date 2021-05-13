N,M,Q = map(int,input().split())
abcd_array = []
for i in range(Q):
    abcd = list(map(int,input().split()))
    abcd_array.append(abcd)
max_point = 0
for a in range(1,M+1):
    for b in range(a,M+1):
        for c in range(b,M+1):
            for d in range(c,M+1):
                for e in range(d,M+1):
                    for f in range(e,M+1):
                        for g in range(f,M+1):
                            for h in range(g,M+1):
                                for i in range(h,M+1):
                                    As = [1,a,b,c,d,e,f,g,h,i]
                                    point = 0
                                    for j in range(Q):
                                        if As[abcd_array[j][1]-1] - As[abcd_array[j][0]-1] == abcd_array[j][2]:
                                            point += abcd_array[j][3]
                                        if j == Q-1 and max_point < point:
                                            max_point = point
print(max_point)
