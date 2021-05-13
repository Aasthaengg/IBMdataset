n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
ret, tmp_temp = 1, h[0]
for i, height in enumerate(h):
    x = t - height*0.006
    if abs(a-x) <= abs(a-tmp_temp):
        tmp_temp = x
        ret = i+1
print(ret)  