from collections import deque
def main(): 
    n = int(input())
    dq = deque([])
    dq.append([0])
    for _ in range(n-1):
        l = len(dq)
        for __ in range(l):
            s = dq.popleft()
            ls = len(set(s))
            for i in range(ls+1):
                dq.append(s+[i])
    
    for s in dq:
        s = list(map(lambda x: chr(x+ord("a")),s))
        print("".join(s))
main()