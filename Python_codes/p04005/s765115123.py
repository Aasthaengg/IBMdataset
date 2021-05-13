l,h,b = map(int,raw_input().split())
print min((l*h)*(b%2),(l*b)*(h%2),(h*b)*(l%2))