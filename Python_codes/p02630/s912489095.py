N = int(input())
a = list(map(int,input().split()))
Q = int(input())
cnt = [0]*1000001
result = 0
for i in a:
    cnt[i] += 1
    result += i
for j in range(Q):
    b,c = map(int,input().split())
    cnt[c] += cnt[b]
    n = cnt[b]
    cnt[b] = 0
    result += (c-b)*n
    print(result)

