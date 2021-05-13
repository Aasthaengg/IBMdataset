N, K = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse = True)

sum = 0
cnt = 0
while K > cnt:
    sum += l[cnt]
    cnt += 1
print(sum)
