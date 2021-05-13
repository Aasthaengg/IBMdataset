N=list(map(int,input().split()))
N.append(N[0]-1)
N.append(N[1]-1)
N.sort(reverse=True)

print(sum(N[0:2]))

