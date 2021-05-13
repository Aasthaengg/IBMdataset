N = int(input())
lis = list(map(int, input().split()))
H_lis = []
H = lis[0]
cnt = 0

if N == 1:
    print(0)
    exit()

for i in lis[1:]:
    if i <= H:
       cnt += 1
       H = i
       H_lis.append(cnt)
    else:
        H_lis.append(cnt)
        cnt = 0
        H = i

print(max(H_lis))