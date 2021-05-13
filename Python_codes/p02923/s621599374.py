N = int(input())
H = list(map(int,input().split()))
Max=0
cnt = 0
H_pre = 0
for Hi in H:
    if Hi <= H_pre:
        cnt += 1
        if cnt >= Max:
            Max = cnt
    else:
        cnt = 0
    H_pre = Hi
print(Max)