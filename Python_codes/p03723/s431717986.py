a,b,c=map(int,open(0).read().split())
e=(a-b)|(b-c)
print(bool(e|(a|b|c)%2)*(e^~-e).bit_length()-1)