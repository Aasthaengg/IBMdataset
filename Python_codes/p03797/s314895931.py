def slove(n, m):
    tmp = n if n < m // 2 else m // 2
    tmp2 = (m - tmp * 2) // 4
    return tmp + tmp2
    
if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    print(slove(n, m))
