hen = list(map(int, input().split()))

naname = max(hen)

if naname == hen[0]: print(int(hen[1]*hen[2]/2))
elif naname == hen[1]: print(int(hen[0]*hen[2]/2))
else: print(int(hen[1]*hen[0]/2))