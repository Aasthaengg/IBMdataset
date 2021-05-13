i = input
n = int(i())
s, t = i(), i()
print(2*n - max(j*(s[-j:]==t[:j]) for j in range(n+1)))