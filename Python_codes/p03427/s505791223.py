N = list(map(int,list(input())))
ans = max(sum(N),N[0]-1+9*(len(N)-1))
print(ans)
