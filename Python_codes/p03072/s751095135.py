n,*h=map(int,open(0).read().split());print(sum(max(h[:x+1])==h[x]for x in range(n)))