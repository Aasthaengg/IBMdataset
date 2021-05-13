def find_lcm(a, b):
    """lcm = least common multiple
    """
    large_num = max(a, b)
    small_num = min(a, b)

    count = 1
    while True:
        
        if large_num * count % small_num == 0:
            break
        count += 1
    
    return large_num * count

if __name__ == "__main__":
    A, B = map(int, input().split())
    print(find_lcm(A, B))