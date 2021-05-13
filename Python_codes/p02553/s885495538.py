abcd = list(map(int,input().split()))

ac=abcd[0]*abcd[2]
ad=abcd[0]*abcd[3]
bc=abcd[1]*abcd[2]
bd=abcd[1]*abcd[3]

maxnum=ac

if maxnum<ad:
    maxnum=ad
if maxnum<bc:
    maxnum=bc
if maxnum<bd:
    maxnum=bd

print(maxnum)