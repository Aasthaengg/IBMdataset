import math
N = int(input())
saidai = math.sqrt(2*N)
saidai = math.floor(saidai)
if saidai*saidai+saidai == 2*N:
    for i in range(1, saidai+1):
        print(i)
elif saidai*saidai+saidai < 2*N:
    saidai = saidai+1
    huyou = saidai*saidai+saidai-2*N
    if huyou % 2 == 0:
        huyou //= 2
        for i in range(1, saidai+1):
            if i == huyou:
                continue
            print(i)
    else:
        huyou = huyou//2+1
        for i in range(2, saidai+1):
            if i == huyou:
                continue
            print(i)
else:
    for i in range(saidai, 0, -1):
        if i*i+i < 2*N:
            newsaidai = i+1
            break
    saidai = newsaidai
    huyou = saidai*saidai+saidai-2*N
    if huyou % 2 == 0:
        huyou //= 2
        for i in range(1, saidai+1):
            if i == huyou:
                continue
            print(i)
    else:
        huyou = huyou//2+1
        for i in range(2, saidai+1):
            if i == huyou:
                continue
            print(i)