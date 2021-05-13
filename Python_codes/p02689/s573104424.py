#import time

def main():
    N, M = map(int, input().split())
    Hs = [0]+list(map(int, input().split()))
    As = [list(map(int, input().split())) for _ in range(M)]

    edge = [{0} for _ in range(N+1)]
    for i in range(M):
        j, k = As[i]
        edge[j].add(Hs[k])
        edge[k].add(Hs[j]) 
    
    tru = [True] * (N+1)
    #s = {0,1}
    #print(edge)   
    for i, s in enumerate(edge):
        if len(s)==1:
            if 0 in s: continue
        ma = int(max(s))
        if ma >= Hs[i]:
            tru[i] = False
    
    ans = tru.count(True)-1

    return ans

if __name__ == '__main__':
    #start = time.time()
    print(main())
    #elapsed_time = time.time() - start
    #print("経過時間:{}".format(elapsed_time * 1000) + "[msec]")