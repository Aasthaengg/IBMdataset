n =  int(input())
p = list(map(int, input().split()))
cnt = 0

for i in range(n-2):
    P = p[i:i+3]
    if P[0] < P[1] < P[2]:
        cnt += 1
    elif P[2] < P[1] < P[0]:
        cnt += 1
        
print(cnt)