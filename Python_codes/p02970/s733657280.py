n,d=map(int,input().split())

shubihani=2*d + 1

tmp = n // shubihani
if n % shubihani != 0:
    tmp += 1
print(tmp)