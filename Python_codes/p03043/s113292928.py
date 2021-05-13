def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N, K = MI()
p = 0

for i in range(1, N + 1):
    p_i = 1 / N
    ex = 0
    
    if i < K: 
        while 1:
            ex += 1
            if i * pow(2, ex) >= K:
                break
    
    p += p_i * (1 / 2)**ex
    
print(p)