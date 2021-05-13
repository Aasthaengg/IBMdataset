N = int(input())
a = list(map(int, input().split()))
decided = [0 for _ in range(N+1)]

a.insert(0,0)

for i in range(N,0,-1):
    count = 0
    check = 2*i
    while check <= N:
        count = (count+decided[check])%2
        check += i
    if a[i] == 1 and count == 1:
        continue
    elif a[i] == 0 and count ==0:
        continue
    else:
        decided[i] = 1

print(sum(decided))
answer = [i for i in range(N+1) if decided[i]==1]

print(" ".join(list(str(i) for i in answer)))