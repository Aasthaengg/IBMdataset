a,b = list(map(int,input().split()))

gap = b-a

def sum_m(a):
    l=0
    for i in range(1,a+1):
        l+=i
    return l

n_b = sum_m(gap)
print(n_b-b)