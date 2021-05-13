from collections import defaultdict
def build_tree(N, edges):
    root_list = [i for i in range(N)]
    for p, q in edges:
        p -= 1
        q -= 1
        root_p = get_root(root_list, p)
        root_q = get_root(root_list, q)
        root_now = min(root_p, root_q, p)
        root_list[p] = root_now
        root_list[q] = root_now
        root_list[root_p] = root_now
        root_list[root_q] = root_now
    return root_list

def get_root(root_list, city):
    if root_list[city] == city:
        return city
    else: 
        root_list[city] = get_root(root_list, root_list[city])
        return root_list[city]

if __name__ == '__main__':
    N, K, L = map(int, input().split())
    roads = [None]*K
    rails = [None]*L
    for k in range(K):
        roads[k] = list(map(int, input().split()))
    for l in range(L):
        rails[l] = list(map(int, input().split()))
    
    
    '''N = 2*10**5
    L = int(N/2)
    K = int(N/2)
    roads = [None]*K
    rails = [None]*L
    for i in range(L):
        roads[i] = [2*i, 2*i+1]
    for i in range(K):
        rails[i] = [2*i, 2*i+1]'''
    
    road_roots = build_tree(N, roads)
    rail_roots = build_tree(N, rails)
    
    railroads = defaultdict(int)
    RR = []
    for n in range(N):
        rr = (get_root(road_roots, n), get_root(rail_roots, n))
        RR.append(rr)
        railroads[rr] += 1
    answer = [railroads[key] for key in RR]
    print(' '.join(map(str, answer)))