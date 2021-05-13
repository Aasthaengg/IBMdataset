N = int(input())
A = [int(a) for a in input().split()]

def devisible(n):
    count = 0
    while n % 2 == 0:
        n /= 2
        count += 1
    return count

print(min(map(devisible, A)))