import sys
sys.setrecursionlimit(10000)
def resolve():
    s = input()
    K = int(input())
    mem = []
    for i in range(1, K+1): # window size
        for j in range(len(s)): # window starts at
            subs = s[j:j+i]
            if subs not in mem:
                mem.append(subs)
    mem.sort()
    # print(mem)
    print(mem[K-1])
    
    
if '__main__' == __name__:
    resolve()