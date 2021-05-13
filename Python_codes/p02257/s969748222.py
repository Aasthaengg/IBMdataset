def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x%2==0:
        return False
    i = 3
    while i <= x**(0.5):
        if x%i==0:
            return False
        i+=2
    return True

if __name__=='__main__':
    N=int(input())
    cnt=0
    for _ in range(N):
        if is_prime(int(input())): cnt+=1
    print(cnt)