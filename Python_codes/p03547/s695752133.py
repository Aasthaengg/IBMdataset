def f(a,b):
  	if  a == b:
  		return '='
  	if a > b:
  		return '>'
  	return  '<'
print f(*raw_input().split())