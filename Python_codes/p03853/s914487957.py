#B - たてなが
H,W = map(int,input().split())
C = []
for _ in range(H):
    Ci = input()
    C.append(Ci)

C_ans = []
for j in range(H):
    C_ans.append(C[j])
    C_ans.append(C[j])

for k in C_ans:
    print(''.join(k))