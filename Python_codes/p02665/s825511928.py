N=int(input())
A_list = list(map(int, input().split()))

if N == 0:
    print(1 if A_list[0] == 1 else -1)
    exit()
    
if A_list[0] >=1:
    print(-1)
    exit()


# 成り立つ木が作れるか判定してみる
en = [0]
en[0] = 1

for a in A_list:
    tmp = en[-1] - a
    if tmp < 0:
        print(-1)
        exit()
    en.append(tmp * 2)

en = en[:-1]

branch = A_list[-1]
res = A_list[-1]
nodes = en[-1]
for a, ena in zip(A_list[-2::-1], en[-2::-1]):
    branch = min(branch+a, ena)
    res += branch

print(res)
