def check7s(k):
    x = 7 % k
    for i in range(1, k + 1):
        if x == 0: return i

        x = (x * 10 + 7) % k
 
    return -1

K = int(input())
print(check7s(K))