N = int(input())
P = list(map(int,input().split()))

last_ok_postion = 0 
count = 1

for i in range(1,N):
    if P[last_ok_postion] >= P[i]:
        m = min(P[last_ok_postion:i])
        if m >= P[i]:
            count += 1
            last_ok_postion = i
print(count)