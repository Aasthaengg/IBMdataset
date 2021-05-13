coins, req = map(int,input().split())

fax = 500*coins >= req

if fax: print("Yes")
else: print("No")