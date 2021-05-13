N, M  = map(int, input().split())

hand = max(N-M,0)
tho  = M

base = tho*1900+hand*100

print(base*(2**tho))