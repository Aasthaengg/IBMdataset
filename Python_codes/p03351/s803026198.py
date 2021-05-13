import sys
input = sys.stdin.readline
a,b,c,d = [int(i) for i in input().split()]
dab =abs(b-a)
dbc = abs(b-c)
ans = "No"
dac = abs(a-c)
if (dab <=d and dbc <= d) or dac<=d :
    ans = "Yes"
print(ans)