from functools import reduce;s, p = input().strip(), input().strip();
print( "Yes" if reduce(lambda a,b: a or b , [ (s[i:]+s[:i]).find(p) > -1 for i in range(0, len(s)) ] ) else "No" )
