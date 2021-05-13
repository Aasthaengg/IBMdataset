h,m,a,b,k=map(int,input().split())
h_to_min = h * 60
a_to_min = a * 60
re1 = a_to_min - h_to_min
re2 = b - m
re = re1 + re2
print(re-k)