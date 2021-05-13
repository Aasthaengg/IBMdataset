def is_prime(n):
    n = abs(n)
    if n==2: return True
    if n<2 or n%2==0: return False
    return pow(2, n-1, n) == 1

cnt = 0
for i in range(int(input())):
    if is_prime(int(input())): cnt+=1
print(cnt)