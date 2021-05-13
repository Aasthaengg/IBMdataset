a,b,c = (int(T) for T in input().split())
print(['NO','YES'][(c-b)==(b-a)])