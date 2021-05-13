import sys
sys.setrecursionlimit(1000000)

def neighbor(N, edges):
    neighbor_list = [[] for _ in range(N)]
    for a, b in edges:
        neighbor_list[a-1] += [b-1]
        neighbor_list[b-1] += [a-1]
        
    return neighbor_list


def paint(K, nlist, now_num, from_num, case_num):
        mod = 1000000007
        if  from_num == -1:
            can_use_color = K - 1
        else:
            can_use_color = K - 2
        
        if len(nlist[now_num]) - 1 > can_use_color:
            return 0
        
        for child in nlist[now_num]:
            if child == from_num:
                continue
            else:
                case_num *= can_use_color
                can_use_color -= 1
                case_num %= mod
        
        for child in nlist[now_num]:
            if child == from_num:
                continue
            else:
                case_num = paint(K, nlist, child, now_num, case_num)
        return case_num%mod
            

if __name__ == '__main__':
    N, K = map(int, input().split())
    edges = [None]*(N-1)
    
    for i in range(N-1):
        edges[i] = list(map(int, input().split()))
    
    nlist = neighbor(N, edges)


    print(paint(K, nlist, 0, -1, K))