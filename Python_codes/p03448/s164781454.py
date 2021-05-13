a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0
a_min = min( x//500 ,a)
for ai in range(a_min+1):
    rem_a = x - (ai * 500)
    if rem_a == 0:
        cnt+=1
        break
    b_min = min( rem_a//100 ,b)
    for bi in range(b_min+1):
        rem_b = rem_a - (bi * 100)
        if rem_b == 0 :
            cnt+=1
            break
        if (rem_b % 50 == 0 and rem_b // 50 <= c ):
            cnt+=1
            continue
print(cnt)