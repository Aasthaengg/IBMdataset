from fractions import Fraction
N,T,A,*HH = map(Fraction, open(0).read().split())
print(int(min(enumerate(HH), key=lambda x:abs(T-x[1]*Fraction('0.006')-A))[0]+1))