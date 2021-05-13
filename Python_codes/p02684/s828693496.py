n,k = map(int,input().split())

t = list(map(int,input().split()))

memo = [0]*(n+1)

for i in range(n):
    memo[i+1] = t[i]

move = 1

count = 0

check = [0]*(n+1)

while check[move] == 0 and count < k-1:
    check[move] += 1
    move=memo[move]
    count += 1

if k == count:
    print(memo[move])
else:
    count2 = 0
    check = [0]*(n+1)
    move_log = []
    while check[move] == 0:
        move_log.append(move)
        check[move] += 1
        move=memo[move]
        count2 += 1
    print(move_log[(k-count)%count2])
