def solve():
    N = int(input())
    score = 0
    for i in range(1, N+1):
        score += i
        if score >= N:
            break
    x = score - N
    res = list(range(1, x)) + list(range(x+1, i+1))
    return '\n'.join(map(str, res))
    
print(solve())