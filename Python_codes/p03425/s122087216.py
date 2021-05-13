N = int(input())
S = [input()[0] for i in range(N)]
m = S.count("M")
a = S.count("A")
r = S.count("R")
c = S.count("C")
h = S.count("H")
print(m*a*r + m*a*c + m*a*h + m*r*c + m*r*h + m*c*h + a*r*c + a*r*h + a*c*h + r*c*h)