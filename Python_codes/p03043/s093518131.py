#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n, k = map(int, input().split())

ans1 = 0
ans2 = 0
for i in range(1, n+1):
    num = 0
    score = i
    if (i >= k):
        ans1 += 1
    else:
        while True:
            score *= 2
            num += 1
            if (score >= k):
                break
        ans2 += (0.5)**num
print((ans1+ans2)/n)

