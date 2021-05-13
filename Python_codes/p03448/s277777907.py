a,b,c,d = map(int, open(0))
print(sum(500*x+100*y+50*z==d for x in range(a+1) for y in range(b+1) for z in range(c+1)))