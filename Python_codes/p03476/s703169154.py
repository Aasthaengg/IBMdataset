def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    max_n = 100005
    is_prime = [True]*max_n
    is_prime[0], is_prime[1] = False, False
    i = 2
    while i*i < max_n:
        if is_prime[i]:
            k = 2
            while i*k < max_n:
                is_prime[i*k] = False
                k+= 1
        i+= 1
        
    table = [0]*max_n
    for i in range(3, max_n):
        table[i] = table[i-1]
        if is_prime[i] and is_prime[(i+1)//2]:
            table[i] += 1
    q = int(input())
    for i in range(q):
        l, r = map(int, input().split())
        tmp = table[r]-table[l]
        if is_prime[l] and is_prime[(l+1)//2]:
            tmp += 1
        print(tmp)



            



if __name__ == '__main__':
    main()