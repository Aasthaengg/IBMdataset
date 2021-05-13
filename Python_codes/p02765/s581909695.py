n, r = map(int,input().split())

if n >= 10:
    in_rate = r
elif n < 10:
    in_rate = r + 100*(10-n)
    
print(in_rate)