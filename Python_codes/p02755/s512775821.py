a,b = map(int, input().split())

genka_8_min=a*12.5
genka_8_max=(a+1)*12.5

if not genka_8_min.is_integer():
    genka_8_min=int(genka_8_min+1)

if genka_8_max.is_integer():
    genka_8=list(range(int(genka_8_min),int(genka_8_max)))
else:
    genka_8=list(range(int(genka_8_min),int(genka_8_max)+1))

genka_10_min=b*10
genka_10_max=(b+1)*10
genka_10=list(range(int(genka_10_min),int(genka_10_max)))

ans=set(genka_8)&set(genka_10)

if len(ans)==0:
    print(-1)
else:
    print(min(ans))