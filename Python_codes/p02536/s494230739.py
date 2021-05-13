from sys import setrecursionlimit
from collections import Counter
import networkx as nx
setrecursionlimit(1000000)
def l_in(type_): return list(map(type_, input().split()))
def i_in(): return int(input())
def m_in(type_): return map(type_, input().split())
def r_in(n, type_): return [type_(input()) for _ in range(n)]

def find_components(n, connectors):
    g = nx.Graph()
    for i in range(n): g.add_node(i+1)
    g.add_edges_from(connectors)
    return len(list(nx.connected_components(g)))


n, m = m_in(int)
ab = [list(m_in(int)) for _ in range(m)]

ans = find_components(n, ab) - 1

print(ans)
