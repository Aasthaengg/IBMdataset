from string import ascii_lowercase as letters
import sys
data = sys.stdin.read().lower()

num = [data.count(s) for s in letters]
ans = '\n'.join(['{0} : {1}'.format(s,n) for s,n in zip(list(letters),num)])
print(ans)