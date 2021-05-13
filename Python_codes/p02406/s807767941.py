x = input()
o = filter(lambda n: n%3 == 0 or '3' in str(n), range(1,x+1))

print " "+" ".join(map(str,o))