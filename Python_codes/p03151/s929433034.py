N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
diff = [0]*N
sumA = 0
sumB = 0
for i in range(N):
    sa = A[i] - B[i]
    diff[i] = sa
    sumA += A[i]
    sumB += B[i]
if sumA < sumB:
    print(-1)
    exit()
diff.sort(reverse= True)
fixidx = -1
usedI = False
c = 0
usedJ = []
for i in range(N):
    usedI = False
    if diff[i] > 0:
        for j in range(fixidx,-N,-1):
            #print(i,j,diff[i],diff[j])
            if diff[j] < 0:
                if not usedI:
                    usedI = True
                    c += 1
                if diff[i] + diff[j] >= 0:
                    diff[i] += diff[j]
                    diff[j] = 0
                    usedJ.append(j)
                    fixidx = j+1
                    if diff[i] == 0:
                        break
#                    print(i,j,diff[i],diff[j])
                else:
                    diff[j] += diff[i]
                    diff[i] = 0
 #                   print(diff[j])
                    usedJ.append(j)
                    fixidx = j
#                    print(i, j, diff[i], diff[j])
                    break
            elif diff[j] >= 0:
                #print(usedJ)
                print(c+len(set(usedJ)))
                exit()
    else:
        break
#print(c,usedJ)
print(c+len(set(usedJ)))



