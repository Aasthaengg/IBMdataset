S=S={"A":[],"B":[],"C":[]}
for X in S:
    S[X]=list(map(lambda x:x.upper(),input()))

T="A"
try:
    while True:
        T=S[T].pop(0)
except:
    print(T)
