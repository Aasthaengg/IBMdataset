n = int(input())
t, a = map(int, input().split())
H = list(map(int, input().split()))
for i in range(n):
    h = H[i]
    chk = t - h*0.006
    if i == 0:
        ans = chk
        ans_index = i+1
    else:
        if abs(chk - a) < abs(ans - a):
            ans = chk
            ans_index = i+1
print(ans_index)