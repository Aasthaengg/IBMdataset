k, a, b = map(int, input().split())

if b-a <= 2 or k-(a-1) < 2:
    print(k+1)

else:
    cycle = (k-(a-1))//2
    if (k-(a-1))%2 == 0:
        print(a + cycle *(b-a))
    else:
        print(a + cycle *(b-a) +1)
