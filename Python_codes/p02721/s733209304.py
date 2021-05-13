N, K, C = map(int,input().split())
S = input()
workable = []
#はたらける日付を出しとく(後で使う)
for i in range(N):
    if S[i] == 'o':
        workable.append(i+1)

#print(workable)

#j-1日目までに頑張ってはたらいたときの最大値(bfore_j)
bfore_j = {1:0}

work = 0
pas = 0
work_a = []
for j in range(N-1):
    if pas == 0:
        if S[j] == 'o':
            work += 1
            pas = C
            work_a.append(j+1)
            
    else:
        pas -= 1
    bfore_j[j+2] = work

#print(bfore_j)

#j+1日目以降に頑張ってはたらいたときの最大値

after_j = {N:0}


work = 0
pas = 0
for l in range(N):
    if pas == 0:
        if S[N-1-l] == 'o':
            work += 1
            pas = C    
    else:
        pas -= 1

    after_j[N-l-1] = work

#print(after_j)

for m in workable:
    if bfore_j[m] + after_j[m] < K:
        print(m)


            



        

    
