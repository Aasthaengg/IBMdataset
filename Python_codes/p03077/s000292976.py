n,a,b,c,d,e=[int(input()) for _ in range(6)]

if n%min(a,b,c,d,e)==0:
    print(n // min(a,b,c,d,e) + 4)
else:
    print(n // min(a,b,c,d,e) + 5)
