N = int(input())
l = list(map(int,input().split()))

new_l = sorted(l)
half1 = new_l[N//2-1]
half2 = new_l[N//2]

if half1 == half2:
    print(0)
else:
    print(half2-half1)