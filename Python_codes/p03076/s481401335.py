ans = 0
last_v = 0
for i in range(5):
    tmp = int(input())
    if tmp % 10 == 0:
        tmp_v = 0
    else:
        tmp_v = 10 - tmp % 10 
    if tmp_v> last_v:
        last_v = tmp_v
    ans += tmp + tmp_v
print(ans - last_v)