def resolve():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)
        divisors.sort(reverse=True)
        return divisors

    n,m=map(int,input().split())
    c = make_divisors(m)
    for i in c:
        if n>m//i:
            continue
        else:
            print(i)
            break
        
if __name__ == '__main__':
    resolve()