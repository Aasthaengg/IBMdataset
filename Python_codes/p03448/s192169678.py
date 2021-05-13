a,b,c,x=[int(input())+1 for _ in range(4)]
print(sum([1 for i in range(a) for j in range(b) for k in range(c) if 500*i+100*j+50*k==x-1]))