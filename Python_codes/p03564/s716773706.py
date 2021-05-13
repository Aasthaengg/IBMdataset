def add_mult(i, count, N, K):
    if count > N:
        return i
    am1 = add_mult(i*2, count + 1, N, K)
    am2 = add_mult(i+K, count + 1, N, K)
    return min(am1, am2)
    
def main():
    N = int(input())
    K = int(input())
    print(add_mult(1, 1, N, K))
main()
