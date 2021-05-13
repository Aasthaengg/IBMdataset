def main():
    N = int(input())
    H = list(map(int, input().split()))
    
    num_lower = [0]*(N)

    step = 0
    h_right = H[-1]
    for i in range(N-2, -1, -1):
        h = H[i]
        if h >= h_right:
            step += 1
        else:
            step = 0
        num_lower[i] = step
        h_right = h

    print(max(num_lower))
    
main()