n = int(input())
li = list(map(int,input().split()))
ans_li=[10 ** 5 + 1] * n

ans_li[0] = li[0]
for i in range(len(li)-1):
    ans_li[i] = min(li[i], ans_li[i])
    ans_li[i+1] = min(li[i], li[i+1])
ans_li[-1] = li[-1]

print(sum(ans_li))