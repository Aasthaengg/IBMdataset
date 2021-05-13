N = int(input())
D = N if N % 2 == 1 else N+1
edges = [str(i)+" "+str(j) for i in range(1, D)
         for j in range(i+1, D) if i+j != D]
edges2 = [str(v)+" "+str(N) for v in range(1, N)] if N % 2 == 1 else []
print(len(edges)+len(edges2))
print("\n".join(edges+edges2))
