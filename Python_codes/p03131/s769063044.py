k , a , b = map(int,input().split())
if a + 2 >= b:
    print(k+1)
elif a + 2 < b:
    if a > k - 1:
        print(k+1)
    elif a <= k - 1:
        s = k - (a - 1)
        if s % 2 == 0:
            print(b + (s//2 - 1)*(b-a))
        elif s % 2 == 1:
            print(b + (s//2 - 1)*(b-a) + 1)