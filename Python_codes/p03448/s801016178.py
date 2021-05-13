a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0
a_min = min( int(x/500) ,a)
for ai in range(a_min+1):
    rem_a = x - (ai * 500)
    if rem_a == 0:
        cnt+=1
        break
    b_min = min( int(rem_a/100) ,b)
    for bi in range(b_min+1):
        rem_b = rem_a - (bi * 100)
        if rem_b == 0:
            cnt+=1
            break
        c_min = min( int(rem_b/50) ,c)
        for ci in range(c_min+1):
            rem_c = rem_b - (ci * 50)
            if rem_c == 0:
                cnt+=1
                break

print(cnt)