from networkx import*
_,*n=map(str.split,open(0))
print(max(*map(len,[*connected_components(Graph(n))]),1,1))