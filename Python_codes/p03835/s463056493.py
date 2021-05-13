K,S = (int(T) for T in input().split())
Count = 0
for TX in range(0,K+1):
    for TY in range(0,K+1):
        if 0<=(S-TX-TY)<=K:
            Count += 1
print(Count)