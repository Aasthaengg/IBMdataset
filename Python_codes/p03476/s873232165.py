def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

s = [0] * (100001)
for i in range(1, 10**5+1): 
    if i%2 == 1 and is_prime(i) and is_prime((i+1)//2):
        s[i-1] = 1

lst = [0] * (100001)
for i in range(10**5):
    lst[i+1] = lst[i] + s[i]

q = int(input())
for k in range(q):
    l, r = map(int, input().split())
    print(lst[r]-lst[l-1])