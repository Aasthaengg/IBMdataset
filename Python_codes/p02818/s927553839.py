
def cookie(a, b, n):
    
    if a >= n:
        return [a-n, b]
    elif n < a+b:
        
        return[0, b-(n-a)]
    else:
        return [0, 0]

if __name__ == "__main__":
    a, b, n = map(int, input().split())
    j = cookie(a, b, n)
    print(j[0], j[1])

