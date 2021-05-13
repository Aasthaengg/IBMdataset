A,B = (int(T) for T in input().split())
print(['Impossible','Possible'][any(T%3==0 for T in [A,B,A+B])])