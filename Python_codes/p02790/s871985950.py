a,b=input().split()
ab=a*int(b)
ba=b*int(a)
print(ab if ab < ba else ba)