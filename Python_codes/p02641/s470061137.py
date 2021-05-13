x, n = map(int, input().split())
#if n==0:
#    print(x)
p = list(range(n))
p = list(map(int, input().split()))
p_2 = list(range(n))
for i in range(n):
    p_2[i] = x-p[i]
for i in range(100):
    h = p_2.count(i)
    h_2 = p_2.count(-i)
    if h==0 and h_2!=0:
        print(x-i)
        break
    elif h!=0 and h_2==0:
        print(x+i)
        break
    elif h==0 and h_2==0:
        print(x-i)
        break
#if n==0:
#    print(x)