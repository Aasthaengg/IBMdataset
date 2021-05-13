from decimal import Decimal
if __name__ == '__main__':

	a,b = map(Decimal,input().split())

	s = str(a*b)
	ind = s.index(".")
	print(s[:ind])

