N = int(input())
p_list = list(map(int, input().split()))

cnt = 2
for i in range(1,N+1):
    cnt -= 1 if p_list[i-1] != i else 0

if cnt < 0:
    print("NO")
else:
    print("YES")
