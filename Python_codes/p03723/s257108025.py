def ex(x):
    while x%2==0 and x>2:
        x/=2
    if x==2:
        return 0
    else:
        return 1
a,b,c = map(int, input().split())
count = 0
if not ex(a)==ex(b)==ex(c)==0:
    while a%2==0 and b%2==0 and c%2==0:
        temp_a = a
        temp_b = b
        temp_c = c
        a = temp_b/2 + temp_c/2
        b = temp_a/2 + temp_c/2
        c = temp_a/2 + temp_b/2
        count+=1
        if ex(a)==ex(b)==ex(c)==0 or a==b==c:
            count = -1
            break
    print(count)
else:
    print("-1")