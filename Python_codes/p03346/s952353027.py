n = int(input())
p = [int(input()) for _ in range(n)]
dic = [0 for _ in range(n+1)]
for i in p:
    dic[i] = dic[i-1] + 1
print(n - max(dic))