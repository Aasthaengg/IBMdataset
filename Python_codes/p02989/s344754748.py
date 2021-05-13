n=int(input())
d=list(map(int,input().split()))

d_sort = sorted(d)
d_med1 = d_sort[len(d)//2-1]
d_med2 = d_sort[len(d)//2]
print(d_med2-d_med1)