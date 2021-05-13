import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
A = []
xy = [[] for i in range(N)]
for i in range(N):
    A.append(I())
    for j in range(A[i]):
        x,y = LI()
        xy[i].append([x-1,y])

# 人は0-index
# 各人が正直者か不親切な人かで全探索、1…正直者、0…不親切な人

ans = 0
for i in range(2**N):
    B = [[] for _ in range(N)]
    a = 0  # 正直者の人数
    for j in range(N):
        if (i>>j) & 1:  # jが正直者
            B[j].append(1)
            a += 1
            for k in range(A[j]):
                B[xy[j][k][0]].append(xy[j][k][1])
        else:  # jが不親切な人
            B[j].append(0)
    if sum(len(set(B[j])) for j in range(N)) != N:  # この場合矛盾
        continue
    else:
        ans = max(ans,a)

print(ans)