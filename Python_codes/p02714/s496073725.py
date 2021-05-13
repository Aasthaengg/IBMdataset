N = int(input())
S = input().strip()
C = {"R":[],"G":[],"B":[]}
for i in range(N):
    C[S[i]].append(i)
C["B"] = set(C["B"])
cnt = 0
for r in C["R"]:
    for g in C["G"]:
        if r<g:
            i = r
            j = g
        else:
            i = g
            j = r
        cnt += len(C["B"])
        if i-(j-i) in C["B"]:
            cnt -= 1
        if j+(j-i) in C["B"]:
            cnt -= 1
        if (j+i)%2==0 and (j+i)//2 in C["B"]:
            cnt -= 1
print(cnt)