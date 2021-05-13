a,b,c=map(int,input().split())
e=(a-b)|(b-c)
print(bool(e|(a|b|c)%2)*(e^~-e).bit_length()-1)